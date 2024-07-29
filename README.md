# ReadME
Portfolio Project 3 – User Ngozi89 – Code Institute

## Project overview

### Introduction to the project

The program created is an online game. It is called Rock-Paper-Scissors Extended. Compared to the classic rock-paper-scissors game, this version has the additional items Lizard and Spock to add more variety to the game. This variant is known from the TV series "The Big Band Theory". The game is based on chance and luck. You can find more information about the general idea of the game on Wikipedia.
<br>Compared to the classic rock-paper-scissors game.
<br>
[Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors) Leads to the Wikipedia page of rock paper scissors.<br>
Here is the link to my Depolyed project:<br>
[Rock-Paper-Scissors Pokemon](https://py-games-rps-45a939b6cc4b.herokuapp.com/) Leads to my deployed project.

### Contents

[Project overview](#project-overview) \
[Introduction to the project](#introduction-to-the-project) \
[Contents](#contents) \
[Game play](#gameplay) \
[User experience (UX)](#user-experience-ux)\
[User story](#user-story)\
[Target audience](#target-audience)\
[Flow Chart](#flow-chart) \
[Features](#features) \
[Technologies used](#technologies-used) \
[Languages used](#languages-used) \
[Software used](#software-used) \
[Data model](#data-model) \
[Libraries used](#libraries-used) \
[Languages used](#languages-used) \
[Deployment](#deployment) \
[Testing](#testing) \
[Manual testing](#manual-testing) \
[Slack peer group rewiew](#slack-peer-group-rewiew) \
[Validator tests](#validator-tests) \
[Solved bugs](#solved-bugs) \
[Known unsolved bugs](#known-unsolved-bugs) \
[Credits](#credits) \
[Code used](#code-used) \
[Content for the project](#content-for-the-project) \
[Learning materials](#learning-materials) \
[Acknowledgments](#acknowledgments)

### Gameplay

First, the player is asked if he or she wants to play giving option to play or quit. If play choses "y" the game rules will be displayed but if the player input is not "y", the game ends. If player input is y and the game rules is displayed, the player is asked to type ok if he want to go ahead to play the game after reading the rules. If the player input is not "ok", the game end but if the player input is "ok" indicating interest in playing the game, the player is asked to enter his name. This allows the computer to address the player directly. When the game has started, the player chooses from the options of (Rock, Paper, Scissors, Lizard, or Spock). At the same time, the computer also selects its object using a random function.

Here are the criteria according to which the computer chooses:<br>
If player choice is rock and computer choice is 1 which is fire, then it's a tie
Scissors cuts Paper <br>
Paper covers Rock <br>
Rock crushes Lizard <br>
Lizard poisons Spock <br>
Spock smashes Scissors <br>
Scissors decapitates Lizard <br>
Lizard eats Paper <br>
Paper disproves Spock <br>
Spock vaporises Rock <br>
Rock crushes Scissors <br>

The player can play as often as he likes. And It is possible to quit the game after each round.

## User experience (UX)

### Target audience

- People who like Browsergamers.
- People who want to pass some free time.
- People who want to play the game Rock-Paper-Scissors against the computer.

### User story

As a first time user of the game, you want to:
- Play a bug-free game.
- Play a self-explanatory game.
- Be able to navigate easily over the terminal window.
- I would like to be able to read the rules of the game.

As a frequent user of the website, you want to:
- Repeat the game experience.
- Improve the last game result.

Objectives of the website operator is to:
- Provide an easy to navigate and to play game.
- Provide a feedback of all user inputs.
- Provide an error free game.
- Provide an entertaining diversion to pass the time.

How this requirements are met:
- The game will be free to play.
- There will be a welcome screen from which the player can navigate.
- All important elements will be shown in the terminal.
- A response is given to every user input, especially if the input is not expected by the computer.
- The player can see the rules of the game.
- There is always the possibility to quit the game in every stage.


### Features

Start Screen:
 
On the start screen, the player is greeted. You will then be asked if you want to play the game.

![Start screen](images/start-screen.png "Start screen of the program")

Only letters are allowed. If something else is entered or the field is left blank, the game ends and a thank you message appears. This is done so user can chose to contiune or stop

![Start screen error message](images/error-start-screen.png ".")

If a valid input has been entered, the player will see the rules of the game. The program is briefly explained and a menu appears. Here the player can choose to continue or quit. To contiune the game the player input must be "ok" else the game cuts and a thank you message appears.

![Game rlue](images/name-entered.png ".")

![Play screen](images/play-screen.png "Play screen.")


On the start screen, the player is greeted with the ASCII font Rock Paper Scissors Extended. You will then be asked to enter your name.

![User name]()

Only letters are allowed when entering names. If something else is entered or the field is left blank, a message appears: The text field must not be left blank and only letters are permitted!

![Start screen error message](images/error-start-screen.png "Error message when entering a username that is not valid.")

If a valid name has been entered, the player will be addressed personally by name. Then ask to make a choice from the option list. The user can only chose what is in the options list (Rock, Paper, Scissors, Lizard, Spock) If player chose andything that's not in the list, the while-loop will continue running until the player chooses from the option provided.

![]("")

Once the player has made a valid selection, his choice is compared with that of the computer and the winner is announced. The computer's choice and the player's choice are displayed.  If the player has won, this is displayed, if the player loses it will be dsplayed and if it's a tie the player will see.
He is also asked at the end whether he wants to play another round, in which case he chose to enter y, to play again or n to stop. If the player enter y, then the game contiunes but if n the game end and the player can see his score. 

This is a screen when the player wins:<br>

![Win screen](images/you-win.png "Win screen")

This is a screen when the player loses:<br>

![Loose screen](images/you-loose.png "Loose screen")

This is a screen of a draw:<br>

![Draw screen](images/draw-screen.png "Draw screen")

![Quit screen](images/quit-screen.png "Quit screen")

Future Implementations:
- Player result displays why still playing. Example. 
- Game played
- Game won
- Game lost
- Game drawn
- Highscore list: <br>
- Sound Effects: <br>
 As a further improvement, sound effects could be added to the game. This would give the player an even better experience and also appeal to the sense of hearing.

## Technologies used

### Languages used
Python is used for the project. For the landingpage HTML, CSS were used to customised the look.

### Software used
Gitpod - To code the project. <br>
Git - For version control. <br>
Github - To store to project. <br>
Heroku – To deploy the project. <br>
Ci Python Linter – To validate the python code. <br>

### Data model
Data is stored in variables in this project. This includes the user_name which is entered by the player and is also printed in the terminal to address the player by name.<br>
In addition, inputs from the player are processed in the menus.

- random: <br>
The random module is used to let the computer make a random selection between Fire, Wave, Fish, Boat or Grass.

## Deployment
The project was coded with codeinstitute-ide.net, stored on github and then deployed on Heroku. 
That is how the deployment was done:

1.  Pushed the latested code to Github.
2.	Log in to Heroku or create an account first.
3.	Click on the New Button on the dashboard in the top right corner.
4.	Click on "Create new app".
5.	Select the relevant region. In my case, I chose Europe.
6.  Select an app name that does not yet exist on heroku.
7.	Click on the "Create app" button.
8.	Click on the settings tab.
9.	Scroll to the buildpacks and click on "add buildpack," select "Python," and click "Add Buildpack".
10.	Repeat last step and add "node.js" buildpack. <br>
    IMPORTANT: First the python buildpack must be displayed, then the pack from node.js. It can be moved via drag and drop. 
11.	Click on the deploy tab.
12.	Click on Github as the deployment method.
13.	Search for the repository name and click on conncet.
14.	Select Enable Automatic Deploys"
15. Click on "Deploy Branch"
16. Click on the "View" button which leads to the deployed app

## Testing
The page was tested on different ways and different errors came to light.

### Manual testing
I have tested all input options, valid input and non-valid input by the user. These tests were carried out throughout the entire project process. Finally, no more errors occurred. The detailed error messages to the user are also explained in the features section. A description of the bugs can be found in solved and unsolved bugs.


### Validator tests
CI Python Linter test: <br>
This are the common errors that occurred: <br>
- continuation line under-indented for visual indent (fixed) <br>
- line too long <br>
- missing whitespace afte (fixed) <br>
- trailing whitespace (fixed) <br>
- missing whitespace around operator (fixed) <br>
- expected 2 blank lines (fixed) <br>
- blank line contains whitespace (fixed) <br>
- closing bracket does not match visual indentation (fixed) <br>
- multiple spaces after keyword (fixed) <br>
- no newline at end of file (fixed) <br>

All bugs could be fixed:
![CI Python Linter test result](images/ci-python-linter-test.png "CI Python Linter test result")

### Solved bugs
- I tried to check several conditions at the same time with a while loop. So: "while not playerchoice == "fire" or not "wave" or not" . This was the wrong approach. The playerchoice function was modified with a try and expect block. Later in the process I implemented a validation check using a more simple while loop again. Blanks were not taken into account

- In addition, I had formatted an f string incorrectly so that the variables were not displayed correctly in the terminal at first. Improving the formatting could fix this.

### Content for the project
The content of this project was written by Ngozi Omenka. I used wikipedia for general information about the game. The emoji for the game is from [emojicombos](https://emojicombos.com/).

### Learning materials
- All content from Online Course in Full Stack Software Development especially videos about Portfolio Project 3 and ReadME from Code Instituet.

- [youtube](https://www.youtube.com/watch?v=I9h1c-121Uk&t=37s ) Information about the input function.

- [W3Schools](https://www.w3schools.com/python/ref_string_isalpha.asp ) Information on the isalpha method.

- [W3Schools](https://www.w3schools.com/python/ref_string_strip.asp#gsc.tab=0 ) Information on the string method.

- [youtube](https://www.youtube.com/watch?v=HcqgHbvN0EQ) Leads to youtube, with a video about the random module.

- [youtube](https://www.youtube.com/watch?v=46yolPy-2VQ) Leads to youtube, with a video with basic information on python.

- [stackoverflow](https://stackoverflow.com) Leads to stackoverflow website.

- [W3Schools](https://www.w3schools.com/python/) Leads to W3Schools website.

### Acknowledgments
- Slack pear groupe.
- To all people who make their knowledge available for free in the internet, especially on youtube.
- [Bro code](https://www.youtube.com/watch?v=fn68QNcatfo)

**This project is for educational use only and was created for the Code Institute course Full stack software development by Ngozi Omenka.**
