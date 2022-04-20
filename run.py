import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
import time
import os
import sys
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cycle_changes_tracker')
OTHER_PHASE_DATA = SHEET.worksheet('other_phase')
MENSTRUAL_PHASE_DATA = SHEET.worksheet('menstrual_phase')


def typingPrint(text):
    """
    Functions to add typing effect to print statements.
    Taken from www.101computing.net/python-typing-text-effect/
    """

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    """
    Function to add typing effect to input functions.
    Taken from www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system('clear')


def intro():
    """
    Provides a brief introduction to the user and gets the users name.
    """
    typingPrint("                                   Hello...        " +
                "\n\n")
    time.sleep(1)
    typingPrint('                      Welcome to ' + Fore.LIGHTMAGENTA_EX +
                'Cycle Changes Tracker' + Fore.RESET + '!     \
                \n\n')
    time.sleep(1)
    typingPrint('            We know the journey into finding what works for' +
                ' you\n                and' +
                ' your body can be a complicated one...\n\n')
    typingPrint("    Starting a new method of birth control or stopping it" +
                " can be challenging...\n\n")
    time.sleep(1)
    typingPrint("          So we are here to support you all the way" +
                " by helping you log\n                    and track changes" +
                " to your symptoms.\n\n")
    time.sleep(1)
    typingPrint('\n                                Menu loading...\n\n')
    time.sleep(1)
    return clearScreen()

    menu()


def menu():
    """
    Menu showing options available to user to choose from.
    """
    print(Fore.LIGHTMAGENTA_EX + '\n                                    ----')
    print('                                  -------- ')
    print('                               ---- ' + Fore.WHITE + Style.BRIGHT +
          'MENU' + Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' ----')
    print('                                  -------- ')
    print('                                    ----                \n ')
    print(Fore.LIGHTMAGENTA_EX + '                   ----             ----' +
          '             ----')
    print('                 --------         --------         --------')
    print('               ------------     ------------     -------------    ')
    print('          ----- ' + Fore.RED + '1.' + Style.BRIGHT + ' Log In' +
          Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' ----- ' + Fore.RED + '2.' +
          Style.BRIGHT + ' Register' + Fore.LIGHTMAGENTA_EX + Style.NORMAL +
          ' ------ ' + Fore.RED + ' 3.' + Style.BRIGHT + ' Guest' +
          Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' -----')
    print('               ------------     ------------     -------------')
    print('                 --------         --------         --------')
    print('                   ----             ----             ----\n' +
          Fore.RESET)
    print('     ')
    print('     ')

    while True:
        menu_option = input('Please enter ' + Fore.LIGHTMAGENTA_EX +
                            '(1) ' + Fore.WHITE + 'to Login,' +
                            Fore.LIGHTMAGENTA_EX + ' (2) ' + Fore.WHITE +
                            'to Register or ' + Fore.LIGHTMAGENTA_EX +
                            '(3) ' + Fore.WHITE + 'to Continue' +
                            ' as Guest. \n\n')
        if menu_option == '1':
            time.sleep(1)
            typingPrint('\nTaking you to Login...\n\n')
            return login()
        elif menu_option == '2':
            time.sleep(1)
            typingPrint('\nTaking you to Register...\n\n')
            return register()
        elif menu_option == '3':
            time.sleep(1)
            typingPrint("\nGreat, we'll get started. You'll have the option" +
                        " to register at the end if you\nwish!\n\n")
            return cycle_phase()
        else:
            print(f'{menu_option} is not a valid option!\n\n')
            continue


def login():
    """
    Function which takes user to login.
    """

    username = input(Fore.LIGHTMAGENTA_EX + 'Please enter your username:' +
                     '\n\n' + Fore.RESET)
    password_input = input(Fore.LIGHTMAGENTA_EX + '\nPlease enter your' +
                           ' password: \n\n' + Fore.RESET)
    user_worksheet = SHEET.worksheet('user_details')

    if user_worksheet.find(username):
        match = user_worksheet.find(username)
        password = user_worksheet.cell(match.row, 2)
    else:
        print('Username is not valid. Please try again...\n\n')
        return login()

    while True:

        if check_password_hash(password.value, password_input):
            typingPrint('\nWelcome back, ' + Fore.LIGHTMAGENTA_EX +
                        f'{username.capitalize()}' + Fore.RESET +
                        '! You are now logged in!\n\n')
            while True:
                proceed = typingInput('\nPlease enter ' +
                                      Fore.LIGHTMAGENTA_EX +
                                      '(L) ' + Fore.RESET + 'to proceed to' +
                                      ' logging your symptoms, ' +
                                      Fore.LIGHTMAGENTA_EX + '(D) ' +
                                      Fore.RESET + 'to go to your\n' +
                                      'dashboard or ' + Fore.LIGHTMAGENTA_EX +
                                      '(E)' + Fore.RESET + ' to log out: \n\n')
                if proceed == 'l' or proceed == 'L':
                    typingPrint("\nGreat, we'll get started!\n\n")
                    return cycle_phase()
                elif proceed == 'd' or proceed == 'D':
                    time.sleep(1)
                    typingPrint('\nLoading dashboard...\n\n\n')
                    return login_menu(username)
                elif proceed == 'e' or proceed == 'E':
                    time.sleep(1)
                    typingPrint('\nSee you next time, ' +
                                Fore.LIGHTMAGENTA_EX +
                                f'{username.capitalize()}' +
                                Fore.RESET + '!\n\n')
                    typingPrint('Logging out...\n\n')
                    return menu()
                else:
                    print(f'{proceed} is not a valid option!')
                    continue
        else:
            print('Password is incorrect. Please try again...')
            return login()


def register():
    """
    Function which registers users details.
    """

    user = {}

    user['username'] = input(Fore.LIGHTMAGENTA_EX + 'Please enter a' +
                             ' username: \n\n' + Fore.RESET)
    user['password'] = generate_password_hash(input(Fore.LIGHTMAGENTA_EX +
                                                    '\nPlease enter a' +
                                                    ' password: \n\n' +
                                                    Fore.RESET))
    register_user(user)
    username = user['username']

    return username


def register_user(user):
    """
    Function to update user_details worksheet with user data in
    register function.
    """

    user_worksheet = SHEET.worksheet('user_details')
    user_worksheet.append_row([x for x in user.values()])
    typingPrint("\nLovely to meet you, " + Fore.LIGHTMAGENTA_EX +
                f"{user['username'].capitalize()}" + Fore.RESET +
                "! \n\nYour details have been registered" +
                " and you are now logged in...\n\n")

    while True:
        proceed = input('Please enter ' + Fore.LIGHTMAGENTA_EX +
                        '(L)' + Fore.RESET + ' to' +
                        ' log your symptoms, ' +
                        Fore.LIGHTMAGENTA_EX + '(D)' +
                        Fore.RESET + ' to view your ' +
                        'dashboard or ' +
                        Fore.LIGHTMAGENTA_EX + '(E) ' +
                        Fore.RESET + 'to\nlog out:\n\n')
        if proceed == 'l' or proceed == 'L':
            typingPrint("Great, we'll get started!\n\n")
            return cycle_phase()
        elif proceed == 'd' or proceed == 'D':
            typingPrint('\nLoading dashboard...\n\n')
            return login_menu(user)
        elif proceed == 'e' or proceed == 'E':
            typingPrint("\nHope to see you back soon, " +
                        Fore.LIGHTMAGENTA_EX +
                        f"{user['username'].capitalize()}!\n\n")
            typingPrint(Fore.RESET + '\nLogging out...\n\n\n\n')
            time.sleep(1)
            return menu()
        else:
            print(f'{proceed} is not a valid option!\n\n')


def login_menu(user):
    """
    Menu shown once user has logged in.
    """

    print(Fore.LIGHTMAGENTA_EX + '\n\n                                    ' +
          '----')
    print('                                  -------- ')
    print('                               ---- ' + Fore.WHITE + Style.BRIGHT +
          'MENU' + Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' ----')
    print('                                  -------- ')
    print('                                    ----                \n ')
    print(Fore.LIGHTMAGENTA_EX + '                   ----             ----' +
          '             ----')
    print('                 --------         --------         --------')
    print('               ------------     ------------     -------------    ')
    print('        ---- ' + Fore.RED + '1.' + Style.BRIGHT + ' My Symptoms' +
          Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' --- ' + Fore.RED + '2.' +
          Style.BRIGHT + ' Log Symptoms' + Fore.LIGHTMAGENTA_EX +
          Style.NORMAL + ' --- ' + Fore.RED + ' 3.' + Style.BRIGHT +
          ' Exit' + Fore.LIGHTMAGENTA_EX + Style.NORMAL + ' -----')
    print('               ------------     ------------     -------------')
    print('                 --------         --------         --------')
    print('                   ----             ----             ----\n' +
          Fore.RESET)
    print('     ')
    print('     ')

    while True:
        login_menu_option = input('Please enter ' +
                                  Fore.LIGHTMAGENTA_EX + '(1)' +
                                  Fore.RESET + ' to view your ' +
                                  'symptoms ' + Fore.LIGHTMAGENTA_EX +
                                  '(2)' + Fore.RESET + ' to log your' +
                                  ' symptoms or ' +
                                  Fore.LIGHTMAGENTA_EX + '(3)' +
                                  Fore.RESET + ' to\nlog out: \n\n')
        if login_menu_option == '1':
            typingPrint('\nTaking you to view the symptoms you have logged' +
                        ' to date...\n\n')
            return get_data(user)
        elif login_menu_option == '2':
            typingPrint('\nTaking you to log your symptoms...\n\n')
            return cycle_phase()
        elif login_menu_option == '3':
            typingPrint("\nHope to see you back soon!\n\n")
            typingPrint('Logging out...\n\n\n')
            time.sleep(1)
            return menu()
        else:
            print(f'{login_menu_option} is not a valid option!\n\n')
            continue


def cycle_phase():
    """
    User can state whether or not they are on their period.
    Will be provided with relevant questions to answer.
    """

    typingPrint("\nWe'll ask you a few questions related to your" +
                " cycle now...\n\n")
    time.sleep(1)

    while True:
        option = typingInput(Fore.LIGHTMAGENTA_EX + 'Are you on your period' +
                             ' today? Y/N\n\n' + Fore.RESET)
        if option == 'y' or option == 'Y':
            typingPrint("\nWe'll ask you some questions about the symptoms"
                        " you're experiencing today...\n\n")
            return menstrual_phase()
        elif option == 'n' or option == 'N':
            typingPrint("\nWe'll ask you some questions about any symptoms" +
                        " you may be experiencing\ntoday...\n\n")
            return any_other_phases()
        else:
            print(f'{option} is not a valid option!\n\n')
            continue


def menstrual_phase():
    """
    Asks the user if they have experienced this level of pain before in order
    to send data to the worksheet.
    """

    menstrual_phase = {}

    the_date = datetime.now().date()
    dt_string = the_date.strftime("%d/%m/%Y")

    menstrual_phase['Date'] = dt_string

    while True:
        typingPrint(Fore.LIGHTMAGENTA_EX + "Where would you" +
                    " place the level of pain you're" +
                    " experiencing on a scale of\n0 - 10?\n")
        pain_scale = input(Fore.LIGHTWHITE_EX + "(0) No Pain --" + Fore.WHITE +
                           "--" + Fore.RED + "---" + Fore.LIGHTRED_EX +
                           "--- Extremely Painful" + " (10)\n\n" + Fore.RESET)

        if pain_scale.isdigit() and int(pain_scale) > 0:
            typingPrint("\nSorry to hear you're experiencing pain today. " +
                        "It's great that you're\nlogging symptoms, lets hope" +
                        " to change that.\n\n")
            break
        elif pain_scale.isdigit() and int(pain_scale) == 0:
            typingPrint("\nNo pain today? Thats great!\n\n")
            break
        else:
            print(f'{pain_scale} is not a valid option!\n\n')
            continue
    menstrual_phase['Pain'] = pain_scale

    while True:
        pain_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you' +
                                      ' experienced this level of pain' +
                                      ' before? Y/N \n\n' + Fore.RESET)
        if pain_exp_before == 'y' or pain_exp_before == 'Y' or\
                pain_exp_before == 'n' or pain_exp_before == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            print(f'{pain_exp_before} is not a valid option!\n\n')
            continue

    menstrual_phase['Pain Exp Before'] = pain_exp_before

    while True:
        typingPrint(Fore.LIGHTMAGENTA_EX + 'How would you' +
                    ' describe your flow today on a scale' +
                    ' of 1 - 5? \n' + Fore.RESET)
        flow_level = input(Fore.LIGHTWHITE_EX + '(0) None, ' + Fore.WHITE +
                           '(1) Very Light, ' + Fore.RED + '(2)' +
                           ' Light, (3) Medium, ' + Fore.LIGHTRED_EX +
                           '(4) Heavy, (5) Very Heavy?\n\n' + Fore.RESET)
        if flow_level.isdigit() and int(flow_level) >= 0 and\
                int(flow_level) <= 5:
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        elif flow_level.isdigit() and int(flow_level) > 5:
            print(f'{flow_level} is not a valid option!\n\n')
            continue
        else:
            print(f'{flow_level} is not a valid option!\n\n')
            continue

    menstrual_phase['Flow'] = flow_level

    while True:
        flow_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you' +
                                      ' experienced this level of flow' +
                                      ' before? Y/N\n\n' + Fore.RESET)
        if flow_exp_before == 'y' or flow_exp_before == 'Y' or\
                flow_exp_before == 'n' or flow_exp_before == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            print(f"{flow_exp_before} is not a valid option!\n\n")
            continue

    menstrual_phase['Flow Exp Before'] = flow_exp_before

    return update_menstrual_phase(menstrual_phase)


def update_menstrual_phase(menstrual_phase):
    """
    Function that updates the menstrual_phase worksheet with the data
    input from the set of questions asked if the user is on their period.
    """

    new_worksheet = SHEET.worksheet('menstrual_phase')
    new_worksheet.append_row([x for x in menstrual_phase.values()])
    typingPrint('Great! Your symptoms have been updated!\n\n')
    typingPrint("Thank you for logging your symptoms today! We'll return you" +
                " to the main\nmenu now...\n\n\n")
    time.sleep(1)
    return menu()


def any_other_phases():
    """
    User will be asked questions regarding symptoms experienced at other
    phases in their cycle.
    Data added to a dictionary which is sent to the worksheet 'other_phase'.
    """

    any_other_phases = {}

    the_date = datetime.now().date()
    dt_string = the_date.strftime("%d/%m/%Y")

    any_other_phases['Date'] = dt_string

    while True:
        other_phase_pain = typingInput(Fore.LIGHTMAGENTA_EX +
                                       'Are you experiencing any' +
                                       ' pain unrelated to your period?' +
                                       ' Y/N\n\n' + Fore.RESET)
        if other_phase_pain == 'y' or other_phase_pain == 'Y':
            typingPrint("\nSorry to hear you're experiencing pain today." +
                        " We'll log these symptoms\nfor you.\n\n")
            break
        elif other_phase_pain == 'n' or other_phase_pain == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            print(f'{other_phase_pain} is not a valid option!\n\n')
            continue

    any_other_phases['Pain'] = other_phase_pain

    while True:
        other_phase_pain_before = typingInput(Fore.LIGHTMAGENTA_EX +
                                              'Have you experienced pain' +
                                              ' unrelated to your period' +
                                              ' before? Y/N\n\n' + Fore.RESET)
        if other_phase_pain_before == 'y' or other_phase_pain_before == 'Y' or\
            other_phase_pain_before == 'n' or\
                other_phase_pain_before == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            typingPrint(f'{other_phase_pain_before} is not a valid' +
                        ' option!\n\n')
            continue

    any_other_phases['Pain Exp Before'] = other_phase_pain_before

    while True:
        spotting = typingInput(Fore.LIGHTMAGENTA_EX + 'Are you experiencing' +
                               ' any spotting today? Y/N\n\n' + Fore.RESET)
        if spotting == 'y' or spotting == 'Y' or spotting == 'n' or\
                spotting == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            typingPrint(f'{spotting} is not a valid option!\n\n')
            continue

    any_other_phases['Spotting'] = spotting

    while True:
        spotting_exp_before = typingInput(Fore.LIGHTMAGENTA_EX +
                                          'Have you experienced spotting' +
                                          ' before? Y/N\n\n' + Fore.RESET)
        if spotting_exp_before == 'y' or spotting_exp_before == 'Y' or\
                spotting_exp_before == 'n' or spotting_exp_before == 'N':
            typingPrint("\nOkay. We'll log this for you.\n\n")
            break
        else:
            typingPrint(f'{spotting_exp_before} is not a valid option!\n\n')
            continue

    any_other_phases['Spotting Exp Before'] = spotting_exp_before

    return update_any_other_phases(any_other_phases)


def update_any_other_phases(any_other_phases):
    """
    Function that updates the other_phase worksheet with the data
    input from the set of questions asked if the user is at any other phase
    of their cycle.
    """

    new_worksheet = SHEET.worksheet('other_phase')
    new_worksheet.append_row([x for x in any_other_phases.values()])
    typingPrint('Great! Your symptoms have been updated!\n\n')
    typingPrint("Thank you for logging your symptoms today! We'll return" +
                " you to the\nmain menu now...\n\n\n")
    time.sleep(1)
    return menu()


def get_data(username):
    """
    Function that displays the data stored in the worksheet.
    Data from menstrual_phase and other_phase worksheet displayed in tables.
    """

    typingPrint('Loading data...\n\n')

    typingPrint(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Here are all the' +
                ' symptoms you have logged to date during your Menstrual' +
                ' Phase: \n\n' + Style.NORMAL)

    time.sleep(1)

    print('\nDATE ' + Fore.RESET + '= Date symptoms were logged.\n')
    print(Fore.LIGHTMAGENTA_EX + 'P/S ' + Fore.RESET + '= The level of pain' +
          ' you logged on the pain scale between:\n'
          '      0 = (No pain) and 10 = (Extremely Painful).\n')
    print(Fore.LIGHTMAGENTA_EX + 'PEBC ' + Fore.RESET + '= If you' +
          ' have experienced that level of pain before the change in' +
          ' your\nbirth control.\n')
    print(Fore.LIGHTMAGENTA_EX + 'F/L ' + Fore.RESET +
          '= The level of your flow you logged between:\n' +
          '      0 (None) - (5) and Extremely Heavy.\n')
    print(Fore.LIGHTMAGENTA_EX + 'FLEBC ' + Fore.RESET +
          '= If you have experienced that level of flow before' +
          ' the change in your birth control.\n')

    time.sleep(1)

    show_menstrual_phase_data = {
        "Menstrual Phase": SHEET.worksheet("menstrual_phase").get_all_values()}

    print(tabulate(show_menstrual_phase_data, headers='firstrow',
                   floatfmt=".10f",
                   showindex=True,
                   tablefmt="grid"))

    time.sleep(1)

    typingPrint(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '\n\nHere are all the' +
                ' symptoms you have logged to date at any other phase' +
                ' in\nyour cycle: \n\n' + Style.NORMAL)

    time.sleep(1)

    print('\nDATE ' + Fore.RESET + '= Date symptoms were logged.\n')
    print(Fore.LIGHTMAGENTA_EX + 'PAIN ' + Fore.RESET + '=  Any pain' +
          ' you experienced.\n')
    print(Fore.LIGHTMAGENTA_EX + 'PEBC ' + Fore.RESET + '= If you had' +
          ' experienced this pain before the change in your birth' +
          ' control.\n')
    print(Fore.LIGHTMAGENTA_EX + 'SPOTTING ' + Fore.RESET + '= Any spotting' +
          ' you experienced.\n')
    print(Fore.LIGHTMAGENTA_EX + 'SEBC ' + Fore.RESET + '= If you ' +
          'had experienced spotting before the change in your' +
          ' birth control.\n')

    time.sleep(1)

    show_other_phase_data = {
        "All Other Phases": SHEET.worksheet("other_phase").get_all_values()
        }

    print(tabulate(show_other_phase_data, headers='firstrow',
                   floatfmt=".5f",
                   showindex=True,
                   tablefmt="grid",
                   stralign='center'))

    typingPrint("\nIt's great that you're logging your symptoms" +
                "! It's important to" +
                " track\nany changes and is a great step" +
                " towards finding what works best for you.\n\n" +
                "You can use this data when discussing your" +
                " experience with your Gynaecologist\nor GP.")

    while True:
        leave_data = typingInput('\n\nPlease enter' + Fore.LIGHTMAGENTA_EX +
                                 ' (D)' + Fore.RESET +
                                 ' to go to your dashboard or ' +
                                 Fore.LIGHTMAGENTA_EX + '(L)' +
                                 Fore.RESET + ' to log out:' +
                                 '\n\n')
        if leave_data == 'd' or leave_data == 'D':
            typingPrint('\nLoading dashboard...\n\n')
            return login_menu(username)
        elif leave_data == 'l' or leave_data == 'L':
            typingPrint("\nThank you " +
                        "for checking in with" +
                        Fore.LIGHTMAGENTA_EX +
                        " Cycle Changes Tracker" +
                        Fore.RESET + "!\n\n" +
                        "Have a great day, " +
                        Fore.LIGHTMAGENTA_EX +
                        f"{username.capitalize()}!\n\n" +
                        Fore.RESET)
            typingPrint('\nLogging out...\n\n\n\n\n')
            time.sleep(1)
            return menu()
        else:
            print(f'{leave_data} is not a valid option!\n\n')
            continue


def start():
    """
    Title that shows when program is run.
    """
    print(Fore.LIGHTMAGENTA_EX + '\n                       ' +
          '-------------------------------')
    print('                    -------------------------------------')
    print('                  --------' + Fore.RED + Style.BRIGHT +
          ' Cycle Changes Tracker ' + Fore.LIGHTMAGENTA_EX + Style.NORMAL +
          '----------')
    print('                    -------------------------------------')
    print('                       -------------------------------\n' +
          Fore.RESET)


def main():
    """
    All fuctions for the programme.
    """

    start()
    intro()
    menu()

    username = login()
    register_user(username)
    username = register_user()
    get_data(username)
    update_menstrual_phase(menstrual_phase)
    update_any_other_phases(any_other_phases)

main()
