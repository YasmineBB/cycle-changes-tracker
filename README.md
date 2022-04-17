# Cycle Changes Tracker  

## Live Site  

View the app [here](https://cycle-changes-tracker.herokuapp.com/).


## Table of Contents  

## Introduction  

Cycle Changes Tracker is a Command Line Interface programme developed to help women track changes to their cycle upon changing their method of birth control.  

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

- I want to be able to see data of the symptoms I have logged.  

## Logic  



## Features  

### Current Features  

#### Introduction  

![title](./assets/README%20screenshots/Title.png)

At the start up point once the program is run, a title appears followed by an introduction to the application.
 <!-- which, at the end, prompts the user to enter their name and welcomes them. -->

<!-- ![Welcome](./assets/README%20screenshots/Welcome%20message.png) -->

#### Main Menu  

![Menu](./assets/README%20screenshots/Menu.png)

The user is then taken to the main menu where they are presented with three options:

1. *Log In*
2. *Register*
3. *Continue as Guest*

#### Login  

Upon entering (1), the user is prompted to log in with the details used when they registered. Once logged in, the user is welcomed and provided an option to proceed to logging their symptoms, or to go to the menu. This menu is different to the main menu and gives the user three options:

1. *About*
2. *Log Symptoms*
3. *Exit*

I wanted to make sure the user always has a choice in how to proceed at each stage so once they have logged in, they are still given the option to exit if they wish.

#### Register

#### Continue as Guest

I provided an option for the user to continue as guest in order to give the user an idea of what they will get if they are hesitant in registering.  By selecting 'Continue as Guest' the user is taking through the application in the same way, just without logging in or registering first.

#### Menstruation Symptoms Tracker

Upon the user selecting (Y) to being on their period, they are then presented with a selection of questions related to their menstrual phase.  

They are asked:


#### Any Other Phase Symptoms Tracker  

Upon selecting 'N' to being on their period, the user is provided a sequence of questions related to any other symptoms they may be experiencing. I have included only two of the many symptoms women can experience, which are regarding spotting and pain.  


### Future Features to Implement  

There are many features that would really boost the overall functionality of this programme and make it more in depth in assisting with the users concerns. I have listed several which I would, and plan to, implement with more time.

#### Mood Tracker  

Alongside tracking pain and flow level, another feature to implement would be a mood tracker to track the users' mood symptoms.

#### Notepad  

I would also an option for the user to add any notes along the way regarding their symptoms to make it more personalised.

## Technologies and Libraries Used  

- Gitpod was used to develop the programme.
- [Heroku](https://id.heroku.com/login) was used to deploy the site.
- [PEP8 online](http://pep8online.com/) was used to validate my python code.
- [gspread](https://pypi.org/project/gspread/) was used to connect my code to Google Sheets where user data is stored.
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.1.x/) was used to create a password hash for the register user aspect of the programme with the data sent to a Google worksheet.
- [Colorama](https://pypi.org/project/colorama/) was used to add colour to the programme.
- typing print effect
- 

## Testing  

A lot of testing took place throughout the duration of building this project! I planned a lot more for this project and I found I had less of a tendency to procrastinate on front end issues as in previous projects! Having a flowchart also helped me stay on track.  

Throughout the development of the programme, I continuously used print statements at various stages to make sure each step was working. I also tested for errors by inputting incorrect data along the way, for example for each question asked, to ensure no errors were triggered and if they were, I created statements as feedback to the user.
PIC EXAMPLE

### PEP8


## Bugs  

- **Colorama light colours not showing on deployed site**  
  - To add some visuals to the questions asking the user to choose their pain and flow level on a scale, I initially used four colours

## Development  

## Deployment  

### Heroku  

## Credits  

- I used this article from [101 Computing](https://www.101computing.net/python-typing-text-effect/) to implement a typing effect on print and input statements as I believe it provided a nice flow to the programme.  
  
- Huge thank you for the help and support from my amazing mentor Richard Wells as well as tutor support who provided a lot of assistance throughout building this project when I got stuck!

