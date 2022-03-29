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
    typingPrint('Welcome to ' + Fore.MAGENTA + 'Cycle Changes Tracker!\n'+ Fore.RESET)
    time.sleep(1)
    typingPrint('We are here to provide you with that extra support with tracking any changes to your symptoms after changing your method of birth control.\n')
    time.sleep(1)

    name = input('Before we start, lets get acquainted. Please enter your name:\n')
    time.sleep(1)
    typingPrint(f'Lovely to meet you, ' + Fore.MAGENTA + f'{name}!\n')

get_user_name()