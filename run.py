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

user = SHEET.worksheet('user')

data = user.get_all_values()

print(data)



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
    typingPrint('Hello...\n')
    time.sleep(1)
    typingPrint('Welcome to ' + Fore.LIGHTMAGENTA_EX + 'Cycle Changes Tracker' + Fore.RESET + '!\n')
    time.sleep(1)
    # typingPrint('So...\n')
    # time.sleep(1)
    # typingPrint('We know the journey into finding what works for you and your'
    # ' body can be tough...it can be long...and frustrating...\n')
    # time.sleep(1)
    # typingPrint("So we are here to support you all the way on your journey by"
    # " helping you track changes to your symptoms.\n")
    # time.sleep(1)
    # typingPrint("We're here, to help you!\n")
    # time.sleep(1)

    # typingPrint('Before we start, lets get acquainted...\n')
    # time.sleep(1)

    # global name

    # name = typingInput('Please enter your name:\n')
    # time.sleep(1)

    # typingPrint(f'Lovely to meet you, ' + Fore.LIGHTMAGENTA_EX + f'{name}!\n' + Fore.RESET)
    # return name


def update_name(entered_name):
    """
    Update user_name worksheet
    """

    user_worksheet = SHEET.worksheet('user')
    user_worksheet.append_row([entered_name])
    typingPrint('Name has been saved!\n')

    cycle_phase()

def cycle_phase():

    """
    User can state whether or not they are on their period.
    Will be provided with relevant questions to answer.
    """

    typingPrint('Lets begin!\n')

    while True:
        option = typingInput('Are you on your period today? Y/N\n')
        if option == 'y' or option == 'Y':
          typingPrint("We'll ask you some questions about the symptoms"
          " you're experiencing today...\n")
          return on_period()
        elif option == 'n' or option == 'N':
          typingPrint("We'll ask you some questions about any symptoms you may"
          " be experiencing today\n")
        else:
          typingPrint(f'{option} is not a valid input! Please enter either Y or N...\n')

        return False


def on_period():
    """
    User will be asked questions related to the beginning of their cycle.
    Modified to check user input is integer, printing ValueError if not, using https://stackoverflow.com/questions/42338468/how-to-check-if-number-is-string-or-integer-in-python-using-if-else
    """

    global pain_exp_before

    pain_scale = typingInput('Where would you place your level of pain on a scale of 0 - 10? \n')

    try:
        integer = int(pain_scale)

        if integer > 0:
            typingPrint("Sorry to here you're experiencing pain today. It's great "
            "that you're logging symptoms, lets hope to change that.\n")
            return (pain_exp_before)
        elif integer == 0:
            typingPrint('No pain today? thats great! \n')

    except ValueError:
        typingPrint(f'{pain_scale} is not a valid input. Please choose a number from 0 - 10.\n')

    
    pain_exp_before = typingInput('Have you experienced this level of pain before? Y/N \n')

    while True:
        if pain_exp_before == 'y' or pain_exp_before == 'Y' or pain_exp_before == 'n' or pain_exp_before == 'N':
            typingPrint('Okay. This change has been logged.')
            return flow_level
        else:
          return


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


def any_other_phases():

    """
    User will be asked questions regarding symptoms experienced at other phases in their cycle.
    """

def exit():
  print('Thank you for logging your symptoms today. Have a great day and see you tommorow!')
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

    print(Fore.LIGHTMAGENTA_EX + '     -------------------------------')
    print('  -------------------------------------')
    print('--------' + Fore.RED + ' Cycle Changes Tracker ' + Fore.LIGHTMAGENTA_EX + '----------')
    print('  -------------------------------------')
    print('     -------------------------------\n' + Fore.RESET)

start()
name = get_user_name()
update_name(name)
on_period()
exit()
