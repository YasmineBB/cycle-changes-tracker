import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
import time
import os
import sys
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime
from prettytable import PrettyTable
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

# """ Add sheets from worksheet """
# menstrual_phase = SHEET.worksheet('menstrual_phase')
# data = menstrual_phase.get_all_values()
# print(data)


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


def get_user_name():
    """
    Provides a brief introduction to the user and gets the users name.
    """
    typingPrint("                                   Hello...        " +
                "\n\n")
    # time.sleep(1)
    
    # typingPrint('                      Welcome to ' + Fore.LIGHTMAGENTA_EX +
    #             'Cycle Changes Tracker' + Fore.RESET + '!               \
    #             \n\n')
    # # typingPrint('So...\n')
    # # time.sleep(1)
    # typingPrint('We know the journey into finding what works for you and' +
    #             ' your body can be a complicated one...\n\n')
    # # time.sleep(1)
    # # typingPrint('It can be long... and frustrating...\n\n')
    # # time.sleep(1)
    # typingPrint("So we are here to support you all the way" +
    #             " by helping you track changes to your symptoms.\n\n")
    # time.sleep(1)
    
    typingPrint('Menu loading...\n\n')
    time.sleep(1)
    # time.sleep(1)
    # typingPrint("We're here, to help you!\n\n")
    # time.sleep(1)

    # typingPrint('Before we start, lets get acquainted...\n\n')
    # time.sleep(1)

    # global name

    # name = typingInput(Fore.WHITE + '                         Please enter' +
    #                    ' your name:\n\n' + Fore.LIGHTMAGENTA_EX)
    # time.sleep(1)
    # print('\n')
    # typingPrint(Fore.WHITE + '                         Lovely to meet you,' +
    # ' + Fore.LIGHTMAGENTA_EX + f'{name}!\n\n' + Fore.RESET)
    # time.sleep(1)
    # print('\n\n\n')
    # return name
    return clearScreen()

    # menu()


# def update_name(name):
#     """
#     Update user_name worksheet
#     """

#     user_worksheet = SHEET.worksheet('user')
#     user_worksheet.append_row([name])
#     menu()


def menu():
    """
    Menu showing options available to user to choose from.
    """

    print(Fore.LIGHTMAGENTA_EX + '                                    ----')
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
        # print('\n\n\n\n')
        if menu_option == '1':
            print(' ')
            time.sleep(1)
            typingPrint('Taking you to Login...\n\n')
            return login()
            break
        elif menu_option == '2':
            print('\n')
            time.sleep(1)
            typingPrint('Taking you to Register...\n\n')
            return register()
            break
        elif menu_option == '3':
            print('\n')
            time.sleep(1)
            typingPrint("Great, we'll get started. You'll have the option to" +
                        " register at the end if you wish!\n\n")
            return cycle_phase()
            break
        else:
            print(f'{menu_option} is not a valid option!\n\n')
            continue

    # cycle_phase()


def login():
    """
    Function which takes user to login.
    """

    username = input(Fore.LIGHTMAGENTA_EX + 'Please enter your username:' +
                     '\n\n' + Fore.RESET)
    password_input = input(Fore.LIGHTMAGENTA_EX + 'Please enter your' +
                           ' password: \n\n' + Fore.RESET)
    user_worksheet = SHEET.worksheet('user_details')
    

    if user_worksheet.find(username):
        match = user_worksheet.find(username)
        password = user_worksheet.cell(match.row, 2)
    else:
        print('Username is not valid. please try again...\n\n')
        return login()


    while True:

        if check_password_hash(password.value, password_input):
            print(' ')
            typingPrint('Welcome back, ' + Fore.LIGHTMAGENTA_EX +
                  f'{username.capitalize()}' + Fore.RESET + '! You are now logged in!\n\n')
            while True:
                proceed = typingInput('Please select (L) to proceed to logging' +
                                ' your symptoms, (D) to go to your dashboard or' +
                                ' (E) to log out: \n\n')
                if proceed == 'l' or proceed == 'L':
                    typingPrint("Great, we'll get started!\n\n")
                    return cycle_phase()
                    break
                elif proceed == 'd' or proceed == 'D':
                    time.sleep(1)
                    typingPrint('Loading Dashboard...\n\n')
                    return login_menu(username)
                    break
                elif proceed == 'e' or proceed == 'E':
                    print(' ')
                    time.sleep(1)
                    typingPrint(f'See you next time, {username}!\n\n')
                    typingPrint('Logging out...')
                    return menu()
                else:
                    print(f'{proceed} is not a valid option!')
                    continue
        else:
            print('Password is incorrect. Please try again...')
            return login()
    # print(password.value)


def register():
    """
    Function which registers users details.
    """

    user = {}
    user['username'] = input(Fore.LIGHTMAGENTA_EX + 'Please enter a username: \n' + Fore.RESET)
    user['password'] = generate_password_hash(input(Fore.LIGHTMAGENTA_EX + 'Please enter a' +
                                                    ' password: \n' + Fore.RESET))
    user['email'] = input(Fore.LIGHTMAGENTA_EX + 'Please enter your email address: \n' + Fore.RESET)
    # print(user)
    
    register_user(user)
    username = user['username']
    print(username)
    # if username
    return username
    # exit(user, username)


def register_user(user):
    """
    Function to update user_details worksheet with user data in register function.
    """

    user_worksheet = SHEET.worksheet('user_details')
    user_worksheet.append_row([x for x in user.values()])
    print(' ')
    typingPrint("Lovely to meet you " + Fore.LIGHTMAGENTA_EX + f"{user['username'].capitalize()}" + Fore.RESET + "! Your details have been registered" +
          " and you are now logged in...\n\n")

    while True:
                proceed = typingInput('Select (L) to proceed to logging ' +
                                'your symptoms, (D) to view your Dashboard' +
                                ' or (E) to log out:\n\n')
                if proceed == 'l' or proceed == 'L':
                    typingPrint("Great, we'll get started!\n\n")
                    return cycle_phase()
                    break
                elif proceed == 'd' or proceed == 'D':
                    typingPrint('Loading dashboard...\n\n')
                    # return clearScreen()
                    return login_menu(user)
                    break
                elif proceed == 'e' or proceed == 'E':
                    print('\n')
                    typingPrint("Hope to see you back soon, " + Fore.LIGHTMAGENTA_EX + f"{user['username'].capitalize()}!\n\n")
                    time.sleep(1)
                    return menu()
                else:
                    print(f'{proceed} is not a valid option!\n\n')
    login_menu(user)


def login_menu(user):
    """
    Menu shown once user has logged in.
    """

    print(Fore.LIGHTMAGENTA_EX + '                                    ----')
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
        login_menu_option = typingInput('Please enter (1) to View Your Symptoms' +
                                        ' (2) to Log Your Symptoms or (3)' +
                                        ' to Exit\n\n')
        # print('\n\n\n\n')
        if login_menu_option == '1':
            # print('\n')
            typingPrint('Taking you to view the symptoms you have logged to date...\n\n')
            return get_data()
            break
        elif login_menu_option == '2':
            print('\n')
            typingPrint('Taking you to Log Your Symptoms...\n\n')
            return cycle_phase()
            break
        elif login_menu_option == '3':
            print('\n')
            typingPrint("Hope to see you back soon, " + Fore.LIGHTMAGENTA_EX + f"{user['username'].capitalize()}!\n\n")
            time.sleep(1)
            return menu()
            break
        else:
            print(f'{login_menu_option} is not a valid option!\n\n')
            continue


def about():
    """
    Funnction creating an about section where the user is directed to
    if choosing to find out more about Cycle Changes Tracker.
    """
    
    
    
    
def cycle_phase():
    """
    User can state whether or not they are on their period.
    Will be provided with relevant questions to answer.
    """

    typingPrint("We'll ask you a few questions related to your cycle now...\n\n")
    time.sleep(1)

    while True:
        option = typingInput(Fore.LIGHTMAGENTA_EX + 'Are you on your period' +
                             ' today? Y/N\n\n' + Fore.RESET)
        print('\n')
        if option == 'y' or option == 'Y':
            typingPrint("We'll ask you some questions about the symptoms"
                        " you're experiencing today...\n\n")
            return menstrual_phase()
        elif option == 'n' or option == 'N':
            typingPrint("We'll ask you some questions about any symptoms" +
                        "you may be experiencing today\n\n")
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
    print(the_date)


    menstrual_phase['Date'] = dt_string

    while True:
        typingPrint(Fore.LIGHTMAGENTA_EX + "Where would you" +
                    " place the level of pain you're" +
                    " experiencing on a scale of 0 - 10?\n")
        pain_scale = input(Fore.LIGHTWHITE_EX + "(0) No Pain --" + Fore.WHITE +
                           "--" + Fore.RED + "---" + Fore.LIGHTRED_EX +
                           "--- Extremely Painful" + " (10)\n\n" + Fore.RESET)

        if pain_scale.isdigit() and int(pain_scale) > 0:
            print('     ')
            typingPrint("Sorry to hear you're experiencing pain today. It's" +
                        " great that you're logging symptoms, lets hope to" +
                        " change that.\n\n")
            break
        elif pain_scale.isdigit() and int(pain_scale) == 0:
            print('     ')
            typingPrint("No pain today? Thats great!\n\n")
            break
        else:
            print(f'{pain_scale} is not a valid option!\n\n')
            continue
    # return pain_scale
    menstrual_phase['Pain'] = pain_scale

    while True:
        pain_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you' +
                                      ' experienced this level of pain' +
                                      ' before? Y/N \n\n' + Fore.RESET)
        if pain_exp_before == 'y' or pain_exp_before == 'Y' or pain_exp_before == 'n' or pain_exp_before == 'N':
            print('     ')
            typingPrint("Okay. We'll log this for you.\n\n")
            # print(pain_exp_before)
            # return on_period_flow_level()
            break
        else:
            print(f'{pain_exp_before} is not a valid option!\n\n')
            continue

    # return pain_exp_before

    menstrual_phase['Pain Exp Before'] = pain_exp_before

    while True:
        typingPrint(Fore.LIGHTMAGENTA_EX + 'How would you' +
                                 ' describe your flow today on a scale' +
                                 ' of 1 - 5? \n' + Fore.RESET)
        flow_level = input(Fore.LIGHTWHITE_EX +
                                 '(0) None, ' + Fore.WHITE + '(1)' +
                                 ' Very Light, ' + Fore.RED + '(2)' +
                                 ' Light, (3) Medium, ' + Fore.LIGHTRED_EX +
                                 '(4) Heavy, (5) Very Heavy?\n\n' + Fore.RESET)
        if flow_level.isdigit() and int(flow_level) >= 0 and int(flow_level) <= 5:
            print('     ')
            typingPrint("Okay. We'll log this for you.\n\n")
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
        if flow_exp_before == 'y' or flow_exp_before == 'Y' or flow_exp_before == 'n' or flow_exp_before == 'N':
            print('     ')
            typingPrint("Okay. We'll log this for you.\n\n")
            # return exit()
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
    exit()


def any_other_phases():
    """
    User will be asked questions regarding symptoms experienced at other
    phases in their cycle.
    Data added to a dictionary which is sent to the worksheet 'other_phase'.
    """

    any_other_phases = {}
    
    the_date = datetime.now().date()
    dt_string = the_date.strftime("%d/%m/%Y")
    print(the_date)


    any_other_phases['Date'] = dt_string

    while True:
        other_phase_pain = typingInput(Fore.LIGHTMAGENTA_EX +
                                       'Are you experiencing any' +
                                       ' pain unrelated to your period?' +
                                       ' Y/N\n\n' + Fore.RESET)
        if other_phase_pain == 'y' or other_phase_pain == 'Y':
            print('\n')
            typingPrint("Sorry to hear you're experiencing pain today." +
                        "We'll log these symptoms for you.\n\n")
            break
        elif other_phase_pain == 'n' or other_phase_pain == 'N':
            print('\n')
            typingPrint("Okay. We'll log this for you.\n\n")
            break
        else:
            print('\n')
            print(f'{other_phase_pain} is not a valid option!\n\n')
            continue

    any_other_phases['Pain'] = other_phase_pain

    while True:
        other_phase_pain_before = typingInput(Fore.LIGHTMAGENTA_EX +
                                              'Have you experienced pain' +
                                              ' unrelated to your period' +
                                              ' before? Y/N\n\n' + Fore.RESET)
        if other_phase_pain_before == 'y' or other_phase_pain_before == 'Y' or other_phase_pain_before == 'n' or other_phase_pain_before == 'N':
            print(' ')
            typingPrint("Okay. We'll log this for you.\n\n")
            break
        else:
            print(' ')
            typingPrint(f'{other_phase_pain_before} is not a valid' +
                        ' option!\n\n')
            continue

    any_other_phases['Pain Exp Before'] = other_phase_pain_before

    while True:
        spotting = typingInput(Fore.LIGHTMAGENTA_EX + 'Are you experiencing' +
                               ' any spotting today? Y/N\n\n' + Fore.RESET)
        if spotting == 'y' or spotting == 'Y' or spotting == 'n' or spotting == 'N':
            print(' ')
            typingPrint("Okay. We'll log this for you.\n\n")
            break
        else:
            print('/n')
            typingPrint(f'{spotting} is not a valid option!\n\n')
            continue

    any_other_phases['Spotting'] = spotting

    while True:
        spotting_exp_before = typingInput(Fore.LIGHTMAGENTA_EX +
                                          'Have you experienced spotting' +
                                          ' before? Y/N\n\n' + Fore.RESET)
        if spotting_exp_before == 'y' or spotting_exp_before == 'Y' or spotting_exp_before == 'n' or spotting_exp_before == 'N':
            print('\n')
            typingPrint("Okay. We'll log this for you.\n\n")
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
    exit()


def get_data():

    print('Loading data...\n\n')
    # get_data = SHEET.worksheet('other_phase').get_all_values()
    # print(get_data)
    # phase_date = OTHER_PHASE_DATA.get_all_records()
    # menstrual_phase_data = 
    
    # phase_data = PrettyTable()
    # phase_data.field_names = ['Date', 'Pain?', 'Pain Exp Before?', 'Spotting?', 'Spotting Exp Before?']
    
    typingPrint(Fore.LIGHTMAGENTA_EX + 'Here are all the symptoms you have logged to date during your Menstrual Phase: \n\n' + Fore.RESET)
    
    show_other_phase_data = {
    "All Other Phases": SHEET.worksheet("other_phase").get_all_values()
    }
    print(tabulate(show_other_phase_data, headers='firstrow',
                   floatfmt=".10f",
                   showindex=True,
                   tablefmt="grid"))
    
    print('    ')
    
    typingPrint(Fore.LIGHTMAGENTA_EX + 'Here are all the symptoms you have logged to date at any other phase in your cycle: \n\n' + Fore.RESET)
    
    show_menstrual_phase_data = { "Menstrual Phase": SHEET.worksheet("menstrual_phase").get_all_values()
                                 }
    
    print(tabulate(show_menstrual_phase_data, headers='firstrow',
                floatfmt=".5f",
                showindex=True,
                tablefmt="grid"))
    
    print(' ')
    typingInput('Select (1) to go to your Dashboard or (2) to Log Out: \n\n')
    
    # print(phase_data)
    
    # start()

    # get_data = OTHER_PHASE_DATA.get_all_records()
    # print(get_data)
    # break

    # exit()


def start():
    """
    Title that shows when program is run.
    """
    print('     ')
    print(Fore.LIGHTMAGENTA_EX + '                       ' +
          '-------------------------------')
    print('                    -------------------------------------')
    print('                  --------' + Fore.RED + Style.BRIGHT +
          ' Cycle Changes Tracker ' + Fore.LIGHTMAGENTA_EX + Style.NORMAL +
          '----------')
    print('                    -------------------------------------')
    print('                       -------------------------------\n' +
          Fore.RESET)


def exit(user, username):
    """
    Exit function to end the application and thank the user for logging \
    their symptoms.
    """
    typingPrint("Thank you for logging your symptoms today, " +
                Fore.LIGHTMAGENTA_EX + f"{user['username']}." + Fore.WHITE +
                " Have a great day and see you tommorow!\n\n")
    time.sleep(1)

    menu()


start()
get_user_name()
# name = get_user_name()
# update_name(name)
menu()

username = login()
register_user(username)
username = login()
exit(user, username)

update_any_other_phases(any_other_phases)

get_data(get_data)

update_menstrual_phase(menstrual_phase)

exit()
