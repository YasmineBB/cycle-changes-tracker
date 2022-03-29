# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

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

def get_user_name():
    """
    Provides a brief introduction to the user and gets the users name.
    """
    print('Hello!\n')
    print('Welcome to Cycle Changes Tracker...\n')
    print('We are here to provide you with that extra support with tracking any changes to your symptoms after changing your method of birth control.\n')

    name = input('Before we start, lets get acquainted. Please enter your name: ')
    print(f'Lovely to meet you, {name}!\n')

get_user_name()