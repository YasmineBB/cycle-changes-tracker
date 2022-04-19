# Cycle Changes Tracker  

![Start-screen](./assets/README%20screenshots/start-screen.png)

## Live Site  

[Cycle Changes Tracker](https://cycle-changes-tracker.herokuapp.com/)

## Table of Contents  
<!-- TOC -->

- [Cycle Changes Tracker](#cycle-changes-tracker)
  - [Live Site](#live-site)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
  - [Logic](#logic)
  - [Features](#features)
    - [Current Features](#current-features)
      - [Run Program](#run-program)
      - [Main Menu](#main-menu)
      - [Register](#register)
      - [Login](#login)
      - [Continue as Guest](#continue-as-guest)
      - [Menstruation Symptoms Tracker](#menstruation-symptoms-tracker)
      - [Any Other Phase Symptoms Tracker](#any-other-phase-symptoms-tracker)
      - [View Your Symptoms](#view-your-symptoms)
    - [Future Features to Implement](#future-features-to-implement)
      - [Mood Tracker](#mood-tracker)
      - [Notepad](#notepad)
      - [Security of Data](#security-of-data)
  - [Data Model](#data-model)
    - [Google Sheets](#google-sheets)
  - [Technologies and Libraries Used](#technologies-and-libraries-used)
  - [Testing](#testing)
    - [PEP8 Validation](#pep8-validation)
    - [Lighthouse Testing](#lighthouse-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
  - [Acknowledgements](#acknowledgements)

<!-- /TOC -->
## Introduction  

Cycle Changes Tracker is a Command Line Interface application developed to help women track their symptoms in order to monitor changes to their cycle upon changing or stopping their method of birth control.

This application runs in a Command Line Interface and has been developed with Python.

I drew upon my own experience as well as that of friends and many other women who face or have faced challenges that come with their menstrual cycle when developing Cycle Changes Tracker. It can be difficult to find what works for each individual as one method that works for one person may not work at all for another, and it can be a long process of testing and trialing different methods. Tracking symptoms is an important approach to take and the concept of Cycle Changes Tracker aims to assist in supporting women along their journey.

## User Experience  

### Target Audience  

The target audience for this programme are:

- Women who have changed or stopped their method of birth control as a means of finding the best option for them in terms of pain management.

- Women who are starting birth control and want to keep track of their symptoms to see if the method is suited to them or whether they need to look at other options.  

Once the change has been made, it is important to monitor and track changes in their symptoms during their cycle following the change in order to feedback to their GP or Gynaecologist, analyse the data and figure out the next point of action.

### User Stories  

Below are some of many scenarios a user may find themselves in which using the Cycle Changes Tracker may prove helpful.  

- *I am changing from a Copper IUD to a Hormonal IUD due to experiencing severe pain during my menstrual cycle and want to track any changes in my symptoms to feedback to my Gynaecologist.*  
  
- *I am experimenting stopping my birth control for a period of time as suggested by my Gynaecologist. They have advised me to monitor any changes to my menstrual flow and pain experienced to feed back to them after 3 months.*  
  
- *I am starting birth control as a means of pain management and need to track my symptoms so, if required to change in the future, I can find the method that works best for me.*  

#### First Time User

- *I want to be able to easily understand what the programme is about.*

- *I want to be able to run through the programme to see how it works before committing to registering.*

- *I want to be asked questions related to the symptoms I experience during my cycle.*

#### Returning User

- *I want to be able to log in.* 

- *I want to be able to log my symptoms intuitively.*

- *I want to be able to view all the symptoms I have logged to date and be presented with data that I can analyse and feed back to my Gynaecologist.*

## Logic  

I created a flowchart to help me plan out the program and to help keep me on track during development which was really useful for me. The flowchart pretty much represents how the programme is run. 

![Flowchart](./assets/README%20screenshots/Flowchart.png)

There are consistent print statements throughout the application providing feedback to the user at each stage. The user is also able to exit or log out at each stage, for example after they have registered, logged in or once they have viewed the data from the dashboard.

![Login-feedback](./assets/README%20screenshots/log%20in%20feedback.png)
## Features

### Current Features  

#### Run Program

![Title](./assets/README%20screenshots/start-up.png)

At the start-up point once the program is run, a title appears followed by an introduction. This introduction addresses the needs of the first time user goal: *"I want to be able to easily understand what the programme is about."*

A message then is printed to notify the user that the menu is loading.

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

To access features such as View Your Symptoms, I recommend registering. However the following details can be entered to log in to test!

- Username - user
- Password - 123

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

This log in system addresses the returning user goal: *"I want to be able to log in."*

#### Continue as Guest

I provided an option for the user to continue as guest to give the user an idea of what they will get if they are hesitant in registering.  By selecting 'Continue as Guest' the user is taken through the application in the same way, just without logging in or registering first.

This addresses the first time user goal of *"I want to be able to run through the programme to see how it works before committing to registering."*

#### Menstruation Symptoms Tracker

Once the user selects to proceed to log their symptoms, they are asked:

- *Are you on your period today? Y / N*

Upon the user selecting (Y) to being on their period, they are then presented with a selection of questions related to their menstrual phase.  

They are asked questions regarding the level of pain and flow they are experiencing and whether they have experienced that level before. At each question the user input is validated, and error messages are presented if an incorrect response is input.

![Error1](./assets/README%20screenshots/error-example-mp.png)


#### Any Other Phase Symptoms Tracker  

Upon selecting 'N' to being on their period, the user is provided a sequence of questions related to any other symptoms they may be experiencing. I have included only two of the many symptoms women can experience, which are regarding spotting and pain. The user is asked if they are experiencing any pain or spotting and if they have experienced those things before at that stage.

The data from both sequences of questions are then sent to the relevant worksheet.

Both of these sequences of questions address the first time user goal: *"I want to be asked questions related to the symptoms I experience during my cycle."* As well as the returning user goal: *"I want to be able to log my symptoms intuitively."*

#### View Your Symptoms  

From the dashboard, the user is provided with the option to view the symptoms they have logged to date.

![View-data-gif](https://media.giphy.com/media/2JJGvHj15yVDah8UGt/giphy.gif)

![View-data-gif2](https://media.giphy.com/media/KCW9tjzBch33Ofy009/giphy.gif)

Before each table of data is presented, there is a confirmation of what each heading term means, as they have been shortened to fit the table but are still meaningful, and what question in the application they refer to.

At the moment and for the purpose of this project, as long as you are registered and logged in with any valid details, the data viewed is all the same as it is linked via API to the two worksheets, so of course the data isn't personalised! In future development the data would be unique to each user.

### Future Features to Implement  

There are many features that would really boost the overall functionality of this programme and make it more in depth in assisting with the users concerns. I have listed several which I would, and plan to, implement with more time.

#### Mood Tracker  

Alongside tracking pain and flow level, another feature to implement would be a mood tracker to track the users' mood symptoms.

#### Notepad  

I would also provide an option for the user to add any notes along the way regarding their symptoms to make it more personalised.

#### Security of Data

For the purpose of this project, apart from generating a password hash there isn't a high level of security in terms of securing user data on screen, as I wasn't able to implement password masking for this project. For example when the user enters their password at the register and login stages, it can be seen on the screen. In the future I would implement a method to mask secure data such as passwords.

## Data Model

### Google Sheets

This application uses Google Sheets to store data that has been inputted by the user.

There are three worksheets:

- One to store data input by the user if they select that they are at the menstrual phase of their cycle.

![menstrual_phase_worksheet](./assets/README%20screenshots/menstrual-phase-worksheet.png)

- One to store data input by the user if they select that they are at any other phase in their cycle.

![other_phase_worksheet](./assets/README%20screenshots/other-phase-worksheet.png)

- A final worksheet contains user login details including username and the hashed password which is sent to the worksheet when the user registers.

## Technologies and Libraries Used  

- [GitHub](https://github.com/YasmineBB/cycle-changes-tracker) was used to create the repository for this project.
- Gitpod was used to develop the programme.
- [Heroku](https://id.heroku.com/login) was used to deploy the site.
- [PEP8 online](http://pep8online.com/) was used to validate my python code.
- [gspread](https://pypi.org/project/gspread/) was used to connect my code to Google Sheets where user data is stored.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) was used to create a password hash for the register user aspect of the programme with the data sent to a Google worksheet.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour to the text in the programme.
- [Tabulate](https://pypi.org/project/tabulate/) was used to create the table that presents the users data.
- *time* and *sys* libraries to create a typing effect for print and input statements.
- *os* library to clear the screen between the introduction and the menu loading.
- *datetime* module to take the date that the user inputs data to send to the menstrual_phase and other_phase worksheets.

## Testing  

A lot of testing took place throughout the duration of building this project! I planned a lot more for this project and I found I had less of a tendency to procrastinate on front end issues as in previous projects! Having a flowchart also helped me stay on track.  

Throughout the development of the programme, I continuously used print statements at various stages to make sure each step was working. I also tested for errors by inputting incorrect data along the way, for example for each question asked, to ensure no errors were triggered and if they were, I created statements as feedback to the user.

### PEP8 Validation

All code has been passed through the PEP8 online checker with no warnings or errors.

![PEP8](./assets/README%20screenshots/PEP8-validation.png)

### Lighthouse Testing

I ran Google Lighthouse testing in an incognito window, and it scores well. Apart from the SEO score which was 89/100, scores are between 90 and 100. However, this application is built purely with Python and I didn't create an HTML file to store meta tags for the site.

Accessibility scores high at 97/100 and apart from the Heroku *Run Program* button, background and foreground colors have a sufficient contrast ratio.

![Lighthouse](./assets/README%20screenshots/lighthouse.png)

## Bugs  

Bugs and errors encountered during development were solved through using print statements and testing along the way at every stage!

Some other fixed bugs include:

- I had some issues after continuing an else statement in one of my while loops. It ran an infinite loop of the else print statement, but this was solved.

- When a user tried to log in, I had an initial problem where if the username wasn't stored in the worksheet, it threw an error rather than the print message in the else statement to request a valid username. Through tutor support assistance this issue was solved.

## Deployment  

### Heroku  

To deploy to Heroku, the following steps are to be followed:

1. Log in to Heroku and navigate to your dashboard.

2. Select "New" at the top right-hand corner.

3. Select "Create new app".

4. Choose a unique name for your app, select your region and click "Create app".

5. Select "Settings" and click "Reveal Config Vars".

6. Create two config vars. For the first one, input "PORT" and "8000" as one, then click add. In the other, input "CREDS" and the content of your Google Sheet API creds file as the other, click add.

7. Click "Add buildpack".

8. Add "nodejs" and "python" from the list and click "Save". Make sure Python is the first buildpack.

9. From the tabs at the top, select "Deploy".

10. Select "GitHub" from Deployment methods.

11. Click "Connect to GitHub".

12. Search for the GitHub repository by the name you gave it.

13. Choose either "Enable Automatic Deploys" or "Deploy Branch" to enable manual deploys.

14. Once loaded, click "View" to view the deployed site.

There was an issue a few days before my project submission deadline with GitHub announcing that a number of security tokens had been compromised in a security breach. Due to changes they had made as a result, I was unable to deploy from the Heroku dashboard. As I had manual deploys enabled, I had to link my app to my Gitpod terminal and deploy from the terminal.

To do this I took the following steps kindly passed on by the Code Institute team:

1. Run the command: *heroku login -i*
2. Log in with email and Heroku password.
3. Run the command: *heroku git:remote -a cycle-changes-tracker*.
4. To deploy, run the command: *git push heroku main*

## Credits  

### Content

- I used this article from [101 Computing](https://www.101computing.net/python-typing-text-effect/) to implement a typing effect on print and input statements as I believe it provided a nice flow to the programme.  

- I used this [Stack Overflow article](https://stackoverflow.com/questions/69472788/how-to-get-columns-titles-from-googlesheets-to-print-in-python) to help me build a table with headings displaying user data from the Google worksheet using Tabulate.

## Acknowledgements  

- Huge thank you for the help and support from my amazing mentor Richard Wells as well as tutor support who provided great assistance throughout building this project when I got stuck!  
