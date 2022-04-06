# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style
import time,os,sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('cycle_changes_tracker')

""" Add sheets from worksheet """

# menstrual_phase = SHEET.worksheet('menstrual_phase')

# data = menstrual_phase.get_all_values()

# print(data)



def typingPrint(text):

  """
  Functions to add typewriter effect.
  Taken from www.101computing.net/python-typing-text-effect/
  """
  
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  

def clearScreen():
  os.system("clear")


def get_user_name():
    """
    Provides a brief introduction to the user and gets the users name.
    """
    typingPrint("                                   Hello...                              \n\n")
    time.sleep(1)
    typingPrint('                      Welcome to ' + Fore.LIGHTMAGENTA_EX + 'Cycle Changes Tracker' + Fore.RESET + '!               \n\n')
    # time.sleep(1)
    # typingPrint('So...\n')
    # time.sleep(1)
    # typingPrint('We know the journey into finding what works for you and your'
    # ' body can be tough...it can be long...and frustrating...\n')
    # time.sleep(1)
    # typingPrint("So we are here to support you all the way on your journey by"
    # " helping you track changes to your symptoms.\n")
    # time.sleep(1)
    # typingPrint("We're here, to help you!\n\n")
    # time.sleep(1)

    # typingPrint('Before we start, lets get acquainted...\n\n')
    # time.sleep(1)

    global name

    name = typingInput(Fore.WHITE + 'Please enter your name:\n\n' + Fore.LIGHTMAGENTA_EX)
    time.sleep(1)
    print('     ')
    typingPrint(Fore.WHITE + f'Lovely to meet you, ' + Fore.LIGHTMAGENTA_EX + f'{name}!\n\n' + Fore.RESET)
    return name


def update_name(entered_name):
    """
    Update user_name worksheet
    """

    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row([entered_name])
    # typingPrint('Name has been saved!\n\n')

    cycle_phase()

def menu():

    print(Fore.LIGHTMAGENTA_EX + '                                    ----')
    print('                                  -------- ')
    print('                               ---- ' + Fore.WHITE + 'MENU' + Fore.LIGHTMAGENTA_EX + ' ----')
    print('                                  -------- ')
    print('                                    ----                \n ')
    
    print(Fore.LIGHTMAGENTA_EX + '                   ----             ----             ----')
    print('                 --------         --------         --------')
    print('               ------------     ------------     -------------    ')
    print('          ----- ' + Fore.RED +  '1. Log In' + Fore.LIGHTMAGENTA_EX + ' ----- ' + Fore.RED + '2. Register' + Fore.LIGHTMAGENTA_EX + ' ------ ' + Fore.RED + ' 3. Guest' + Fore.LIGHTMAGENTA_EX + ' -----')
    print('               ------------     ------------     -------------')
    print('                 --------         --------         --------')
    print('                   ----             ----             ----\n' + Fore.RESET)


    
    # typingPrint('1. Login\n\n')
    # typingPrint('2. Register\n\n')
    # typingPrint('3. Continue as Guest\n\n')
    typingInput('                Please choose an option from the menu above. \n' + Fore.LIGHTMAGENTA_EX + '               (1) ' + Fore.WHITE + 'Login, ' + Fore.LIGHTMAGENTA_EX + '(2) ' + Fore.WHITE + 'Register, ' + Fore.LIGHTMAGENTA_EX + '(3) ' + Fore.WHITE + 'Continue as Guest\n' + Fore.RESET)

    # cycle_phase()

def cycle_phase():

    """
    User can state whether or not they are on their period.
    Will be provided with relevant questions to answer.
    """

    typingPrint('Lets begin!\n\n')

    while True:
        option = typingInput(Fore.LIGHTMAGENTA_EX + 'Are you on your period today? Y/N\n\n' + Fore.RESET)
        print('   ')
        if option == 'y' or option == 'Y':
          typingPrint("We'll ask you some questions about the symptoms"
          " you're experiencing today...\n\n")
          return on_period_pain()
        elif option == 'n' or option == 'N':
          typingPrint("We'll ask you some questions about any symptoms you may"
          " be experiencing today\n\n")
          return exit()
        else:
          typingPrint(f'{option} is not a valid input! Please enter either Y or N...\n\n')

        return False

# global pain_exp_before 

def on_period_pain():
    """
    User will be asked questions related the pain, if any, they are experiencing at the beginning of their cycle.
    Modified to check user input is integer, printing ValueError if not, using https://stackoverflow.com/questions/42338468/how-to-check-if-number-is-string-or-integer-in-python-using-if-else
    """
    pain_scale = typingInput(Fore.LIGHTMAGENTA_EX + "Where would you place the level of pain you're experiencing on a scale of 0 - 10?\n" +
    Fore.LIGHTWHITE_EX + "(0) No Pain --" + Fore.WHITE + "--" + Fore.RED + "---" + Fore.LIGHTRED_EX + "--- Extremely Painful (10)\n\n" + Fore.RESET)

    try:
        integer = int(pain_scale)

        if integer > 0:
            print('     ')
            typingPrint("Sorry to hear you're experiencing pain today. It's great "
            "that you're logging symptoms, lets hope to change that.\n\n")
            return pain_exp()
            # pass
        elif integer == 0:
            print('     ')
            typingPrint("No pain today? Thats great!\n\n")
            return pain_exp()
        # return pain_scale

    except ValueError as e:
        # if integer != int:
            typingPrint(f'{pain_scale} is not a valid input. Please choose a number from 0 - 10.\n\n')
            return on_period_pain()

def update_pain_scale(entered_value):
    """
    Update menstrual_phase worksheet
    """

    menstrual_phase_worksheet = SHEET.worksheet('menstrual_phase')
    menstrual_phase_worksheet.append_row([entered_value])
    typingPrint('Pain scale has been saved!\n')

    # while True:
    #     pain_scale = int(typingInput('Where would you place your level of pain on a scale of 0 - 10?\n'))
    #     if pain_scale.isnumeric() and pain_scale > 0:
    #         typingPrint("Sorry to here you're experiencing pain today. Its great "
    #         "that you're logging symptoms, lets hope to change that.\n")
    #     elif pain_scale.isnumeric() and (pain_scale) == 0:
    #         typingPrint('No pain today? thats great!\n')
    #     else:
    #         typingPrint(f'{pain_scale} is not a valid input. Please choose a number from 0 - 10.\n')
        # else:
        #     return exit()
        
def pain_exp():

    """
    Asks the user if they have experienced this level of pain before in order to log to the worksheet.
    """

    global pain_exp_before

    while True:
        pain_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you experienced this level of pain before? Y/N \n\n' + Fore.RESET)
        if pain_exp_before == 'y' or pain_exp_before == 'Y' or pain_exp_before == 'n' or pain_exp_before == 'N':
          print('     ')
          typingPrint("Okay. We've logged this for you.\n\n")
          return on_period_flow_level()
          break
        else:
          typingPrint(f'{pain_exp_before} is not a valid input! Please enter either Y or N...\n\n')
          continue
        
    return pain_exp_before

def update_pain_exp(entered_value):
    """
    Update menstrual_phase worksheet
    """

    menstrual_phase_worksheet = SHEET.worksheet('menstrual_phase')
    menstrual_phase_worksheet.append_row('A:A',[entered_value])
    typingPrint('Data has been saved!\n')



def on_period_flow_level():

    while True:
        flow_level = typingInput(Fore.LIGHTMAGENTA_EX + 'How would you describe your flow today on a scale of 1 - 5? \n'
        + Fore.LIGHTWHITE_EX + '(0) None, ' + Fore.WHITE +  '(1) Very Light, ' + Fore.RED + '(2) Light, (3) Medium, ' + Fore.LIGHTRED_EX + '(4) Heavy, (5) Very Heavy?\n\n' + Fore.RESET)
        if int(flow_level) >= 0 and int(flow_level) <= 5:
          print('     ')
          typingPrint("Okay. We've logged this for you.\n\n")
          return flow_exp()
          break
        # elif int(flow_level) == False and int(flow_level) >5:
        #   print('     ')
        #   print(f'{flow_level} is not a valid input. Please input a number between 0 and 5.\n')
        #   # print("Okay. We've logged this for you.\n\n")
        #   return flow_exp()
        else:
          # print('     ')
          print(f'{flow_level} is not a valid input. Please input a number between 0 and 5.\n')
          continue

def flow_exp():

    while True:
        flow_exp_before = typingInput(Fore.LIGHTMAGENTA_EX + 'Have you experienced this level of flow before? Y/N\n\n' + Fore.RESET)
        if flow_exp_before == 'y' or flow_exp_before == 'Y' or flow_exp_before == 'n' or flow_exp_before == 'N':
          print('     ')
          typingPrint("Okay. We've logged this for you.\n\n")
          return exit()
          break
        else:
          typingPrint(f"{pain_exp_before} is not a valid input! Please enter either Y or N...\n\n")
          continue


def any_other_phases():

    """
    User will be asked questions regarding symptoms experienced at other phases in their cycle.
    """

def exit():

  typingPrint("Thank you for logging your symptoms today, "  + Fore.LIGHTMAGENTA_EX + f"{name} " + Fore.WHITE + "Have a great day and see you tommorow!\n")
  time.sleep(1)
  start()



# def validate_name_input(values):
#     """
#     Validates that a name has been inputed by the user.
#     """  
#     try:
#         if len(values) < 1 and values.is_not:
#             raise ValueError(
#                 'We need your name to accurately track your symptoms!'
#             )
#     except ValueError as e:
#         typingPrint('Please enter your name: ')

# get_user_name()
# validate_name_input()

# def main():
#     """
#     contains all the functions for the program
#     """
#     get_user_name()

def start():

    """
    Title that shows when program is run.
    """
    print('     ')
    print(Fore.LIGHTMAGENTA_EX + '                       -------------------------------')
    print('                    -------------------------------------')
    print('                  --------' + Fore.RED + ' Cycle Changes Tracker ' + Fore.LIGHTMAGENTA_EX + '----------')
    print('                    -------------------------------------')
    print('                       -------------------------------\n' + Fore.RESET)




start()
name = get_user_name()
update_name(name)

# pain_scale = on_period_pain()
# update_pain_scale(pain_scale)

# pain_exp_before = pain_exp()
# update_pain_exp(pain_exp_before)
# flow_exp()
# on_period()
# exit()
