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

# symptoms = SHEET.worksheet('symptoms')

# data = symptoms.get_all_values()

# print(data)



"""
Functions to add typewriter effect.
Taken from www.101computing.net/python-typing-text-effect/
"""

def typingPrint(text):
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
    typingPrint('Welcome to ' + Fore.LIGHTMAGENTA_EX + 'Cycle Changes Tracker!\n' + Fore.RESET)
    time.sleep(1)
    typingPrint('We are here to provide you with that extra support with tracking any changes to your symptoms after changing your method of birth control.\n')
    time.sleep(1)

    typingPrint('Before we start, lets get acquainted... \n')
    time.sleep(1)
    name = typingInput('Please enter your name: \n')
    time.sleep(1)
    typingPrint(f'Lovely to meet you, ' + Fore.LIGHTMAGENTA_EX + f'{name}!\n' + Fore.RESET)

    cycle_phase()

def cycle_phase():

    """
    User can state whether or not they are on their period.
    Will be provided with relevant questions to answer.
    """

    while True:
        option = input('Are you on your period? Y/N\n')
        if option == 'y' or option == 'Y':
          typingPrint("We'll ask you some questions about the symptoms you're experiencing today...\n")
          on_period()
        elif option == 'n' or option == 'N':
          typingPrint("We'll ask you some questions about any symptoms you may be experiencing today\n")
        else:
          typingPrint(f'{option} is not a valid input. Please enter either Y or N...\n')


def on_period():
  """
  User will be asked questions related to the beginning of their cycle.
  """
  typingPrint('hello\n')
  exit()

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

  print(Fore.LIGHTMAGENTA_EX + '     -------------------------------')
  print('  -------------------------------------')
  print('--------' + Fore.RED + ' Cycle Changes Tracker ' + Fore.LIGHTMAGENTA_EX + '----------')
  print('  -------------------------------------')
  print('     -------------------------------\n' + Fore.RESET)

start()
get_user_name()
on_period()
exit()
