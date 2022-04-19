# Cycle Changes Tracker  

## Live Site  

View the app [here](https://cycle-changes-tracker.herokuapp.com/).


## Table of Contents  

## Introduction  

Cycle Changes Tracker is a Command Line Interface programme developed to help women track changes to their cycle upon changing or stopping their method of birth control.  

This programme runs in a Command Line Interface and has been developed with Python.

## User Experience  

### Target Audience  

The target audience for this programme are:

- Women who have changed their method of birth control as a means of finding the best option for them in terms of pain management.

- Women who are starting birth control and want to keep track of their symptoms to see if the method is suited to them or whether they need to look at other options.  

Once the change has been made, it is important to monitor and track changes in their symptoms during their cycle following the change in order to feedback to their GP or Gynaecologist, analyse the data and figure out the next point of action.

### User Stories  

Below are some scenarios a user may find themselves in which would using the Cycle Changes Tracker may prove helpful.  

- *I am changing from a Copper IUD to a Hormonal IUD due to experiencing severe pain during my menstrual cycle and want to track any changes in my symptoms to feedback to my Gynaecologist.*  
  
- *I am experimenting stopping my birth control for a period of time as suggested by my Gynaecologist. She has advised me to monitor any changes to my menstrual flow and pain experienced to feed back to her after 3 months.*  
  
- *I am starting birth control and want to keep track of my symptoms so, if required to change in the future, I can find the method that works best for me.*  

#### First Time User

- I want to be able to easily understand what the programme is about.  

- I want to be able to run through the programme to see how it works before committing to registering.  

- I want to be asked questions related symptoms during my cycle that I can track and feedback to my Gynaecologist.  

#### Returning User

- I want to be able to log in.  

- I want to be able to log my symptoms intuitively.

- I want to be able to view all the symptoms I have logged to date.  

## Logic  



## Features  

### Current Features  

#### Introduction  

![title](./assets/README%20screenshots/start-up.png)

At the start-up point once the program is run, a title appears followed by an introduction. A message then is printed to notify the user that the menu is loading.

#### Main Menu  

![Menu](./assets/README%20screenshots/Menu.png)

The user is then taken to the main menu where they are presented with three options:

1. *Log In*
2. *Register*
3. *Continue as Guest*


#### Register  

The user has the option to register their details, which are then sent to a Google worksheet using gspread. The user is requested to enter a username and password. I have used the Werkzeug library to generate a password hash for the password the user enters. This hashes the password and stores it in a Google worksheet that contains user details.

Once the user registers their details they receive a welcome message and confirmation that they are now logged in. They are then presented with options to proceed to log their symptoms, to view their dashboard or to log out.

I wanted to make sure the user always has a choice in how to proceed at each stage so once they have registered, and logged in, they are still given the option to log out if they wish.

#### Login  

Upon selecting to log in, the user is prompted to log in with the details entered when they registered.

The username and password entered are checked against the Google worksheet and an error message is presented if both the username and password can't be validated.  

- User Validation
![Login](./assets/README%20screenshots/login.png)

- Password validation
![Login-2](./assets/README%20screenshots/login-2.png)

Once logged in, the user is welcomed and provided with the option to proceed to logging their symptoms, go to the dashboard or log out.

If the user chooses to go to their dashboard, they are presented with the following options:

1. View the symptoms logged to date
2. Log their symptoms
3. Log out

![Dashboard](./assets/README%20screenshots/dashboard.png)

Again, the user has the option to leave the programme if they wish.

#### Continue as Guest

I provided an option for the user to continue as guest in order to give the user an idea of what they will get if they are hesitant in registering.  By selecting 'Continue as Guest' the user is taking through the application in the same way, just without logging in or registering first.

#### Menstruation Symptoms Tracker

Once the user selects to proceed to log their symptoms, they are asked:

- *Are you on your period today? Y / N*

Upon the user selecting (Y) to being on their period, they are then presented with a selection of questions related to their menstrual phase.  

They are asked questions regarding the level of pain and flow they are experiencing and whether they have experienced that level before. At each question the user input is validated and error messages are presented if the wrong data is input.

PIC


#### Any Other Phase Symptoms Tracker  

Upon selecting 'N' to being on their period, the user is provided a sequence of questions related to any other symptoms they may be experiencing. I have included only two of the many symptoms women can experience, which are regarding spotting and pain. The user is asked if they are experiencing and pain or spotting and if they have experienced those things before.

The data from both sequences of questions are then sent to the worksheet.

#### View Your Symptoms  

From the dashboard, the user is provided with the option to view the symptoms they have logged to date. At the moment and for the purpose of this project, as long as you are registered and logged in with any valid details, the data viewed is all the same as it is linked via API to the two worksheets, so of course the data isn't personalised! In future development the data would be unique to each user.

### Future Features to Implement  

There are many features that would really boost the overall functionality of this programme and make it more in depth in assisting with the users concerns. I have listed several which I would, and plan to, implement with more time.

#### Mood Tracker  

Alongside tracking pain and flow level, another feature to implement would be a mood tracker to track the users' mood symptoms.

#### Notepad  

I would also an option for the user to add any notes along the way regarding their symptoms to make it more personalised.

#### Security of Data

For the purpose of this project, there isn't a high level of security in terms of securing user data. For example when the user enters their password at the register and login stages, it can be seen on the screen.

## Technologies and Libraries Used  

- Gitpod was used to develop the programme.
- [Heroku](https://id.heroku.com/login) was used to deploy the site.
- [PEP8 online](http://pep8online.com/) was used to validate my python code.
- [gspread](https://pypi.org/project/gspread/) was used to connect my code to Google Sheets where user data is stored.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) was used to create a password hash for the register user aspect of the programme with the data sent to a Google worksheet.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour to the text in the programme.
- [Tabulate](https://pypi.org/project/tabulate/) was used to create the table that presents the users data.


## Testing  

A lot of testing took place throughout the duration of building this project! I planned a lot more for this project and I found I had less of a tendency to procrastinate on front end issues as in previous projects! Having a flowchart also helped me stay on track.  

Throughout the development of the programme, I continuously used print statements at various stages to make sure each step was working. I also tested for errors by inputting incorrect data along the way, for example for each question asked, to ensure no errors were triggered and if they were, I created statements as feedback to the user.
PIC EXAMPLE

### PEP8

All code has been passed through the PEP8 online checker with no warnings or errors.

![PEP8](./assets/README%20screenshots/PEP8-validation.png)

## Bugs  

- **Colorama light colours not showing on deployed site**  
  - To add some visuals to the questions asking the user to choose their pain and flow level on a scale, I initially used four colours  

- I had some issues after continuing an else statement in a while loop. It ran an infinite loop of the else print statement.  
  
- When a user tried to log in, I had an initial problem where if the username wasn't stored in the worksheet, it threw an AttributeError rather than the print message in the else statement to request a valid username. Through tutor support assistance this issue was solved.

## Development  

## Deployment  

### Heroku  

To deploy to Heroku, the following steps are to be followed:

1. 
## Credits  

- I used this article from [101 Computing](https://www.101computing.net/python-typing-text-effect/) to implement a typing effect on print and input statements as I believe it provided a nice flow to the programme.  
  
- Huge thank you for the help and support from my amazing mentor Richard Wells as well as tutor support who provided a lot of assistance throughout building this project when I got stuck!  
