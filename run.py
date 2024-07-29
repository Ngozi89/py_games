# Import the module
import random


# Welcome message, game rules and player name
print("Welcome to game world")

player = input("Do you want to play Rock, Paper, Scissors game? y/n ")

if player.lower() != "y":
    quit("Thanks for stoping by")
else:
    print("Here is the rules for the game ")
    print(" . The game is between you and the computer")
    print()
    print(" . There are 5 options to chose from (Rock, Paper, Scissors, Lizard, Spock)")
    print()
    print(" . You chose one and computer choses randomly")
    print()
    print(" . If your choice is same as the computer, you lose.")
    print()
    print(" . If your choice beats computer chose, you wine if not you lose")
    print()

player = input(" . If you are ready, type 'ok' ")

if player.lower() != "ok":
    quit("Okay, thanks for stopping by")
else:
    print("Game starts :)")
print()
# Let player enter name
name = input("Enter your name: ").capitalize()
# The strip() method ensures that something has to be entered and
# the isalpha() method ensures that only letters can be entered
while not name.strip() or not name.isalpha():
    name = input("The input field must not be left blank.\n"
                      "The user name must not contain any spaces, "
                      "only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
"Name: "
print("Hi,", str(name) + "!")
# End player name

# Player score
score = 0

# Add player and computer choice
options = ("rock", "paper", "scissors", "lizard", "spock")

# Let user play again
running = True

while running:
    playerchoice = None
    computerchoice = random.choice(options)  # Computer choses randomly

    while playerchoice not in options:  # Keep runing until player chose from optionlist
        playerchoice = input("Make a choice (Rock, Paper, Scissors, Lizard, Spock) ").lower()

    if playerchoice == "rock":
        print('''You chose '''+playerchoice+'''!''')  # Print player choice
        print('''
    ⠀⠀⠀⠀⠀⠀🗿⠀⠀⠀
        ''')

    elif playerchoice == "paper":
        print('''You chose '''+playerchoice+'''!''')  # Print player choice
        print('''📃''')
        print()

    elif playerchoice == "scissors":
        print('''You chose '''+playerchoice+'''!''')  # Print player choice
        print('''✂️''')
        print()

    elif playerchoice == "lizard":
        print('''You chose '''+playerchoice+'''!''')  # Print player choice
        print('''🦎''')
        print()

    if playerchoice == "spock":
        print('''You chose '''+playerchoice+'''!''')  # Print player choice
        print('''🖖''')
        print()

    computerchoice = random.randint(1, 5)  # List computer choice in number 1-5
    if computerchoice == 1:
        print('''The computer chose rock!''')  # print computer choice
        print('''🗿''')
        print()

    elif computerchoice == 2:
        print('''The computer chose paper!''')
        print('''📃''')
        print()

    elif computerchoice == 3:
        print('''The computer chose scissors!''')
        print('''✂️''')
        print()

    elif computerchoice == 4:
        print('''The computer chose lizard!''')
        print('''🦎''')
        print()

    elif computerchoice == 5:
        print('''The computer chose spock!''')
        print('''🖖''')
        print()

    # Add Winner condition
    # Rock
    if playerchoice == "rock" and computerchoice == 1:
        print("It's a tie!")
        print()

    elif playerchoice == "rock" and computerchoice == 2:
        print("You lose! Paper covers Rock")
        print()

    elif playerchoice == "rock" and computerchoice == 3:
        print("Yeah! you win! Rock crushes Scissors")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "rock" and computerchoice == 4:
        print("Yeah! You win, Rock crushes Lizard")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "rock" and computerchoice == 5:
        print("You lose! Spock vaporizes Rock")

    # paper
    elif playerchoice == "paper" and computerchoice == 1:
        print("Yeah! You win, Paper covers Rock")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "paper" and computerchoice == 2:
        print("It's a tie!")
        print()

    elif playerchoice == "paper" and computerchoice == 3:
        print("You lose! Scissors cuts Paper")

    elif playerchoice == "paper" and computerchoice == 4:
        print("You lose! Lizard eats Paper")
        print()

    elif playerchoice == "paper" and computerchoice == 5:
        print("Yeah! You win, Paper disproves Spock")
        print('''👍''')
        print()
        score += 1

    # scissors
    elif playerchoice == "scissors" and computerchoice == 1:
        print("You lose!  Rock crushes Scissors")

    elif playerchoice == "scissors" and computerchoice == 2:
        print("Yeah! you win Scissors cuts Paper")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "scissors" and computerchoice == 3:
        print("It's a tie!")
        print()

    elif playerchoice == "scissors" and computerchoice == 4:
        print("Yeah! You win, Scissors decapitates Lizard")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "scissors" and computerchoice == 5:
        print("You lose! Spock smashes Scissors")
        print()

    # lizard
    elif playerchoice == "lizard" and computerchoice == 1:
        print("You lose! Rock crushes Lizard")
        print()

    elif playerchoice == "lizard" and computerchoice == 2:
        print("Yeah! you win, Lizard eats Paper")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "lizard" and computerchoice == 3:
        print("You lose! Scissors decapitates Lizard")
        print()

    elif playerchoice == "lizard" and computerchoice == 4:
        print("It's a tie!")
        print()

    elif playerchoice == "lizard" and computerchoice == 5:
        print("Yeah! You win, Lizard poisons Spock")
        print('''👍''')
        print()
        score += 1

    # spock
    elif playerchoice == "spock" and computerchoice == 1:
        print("Yeah! You win, Spock vaporizes Rock")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "spock" and computerchoice == 2:
        print("You lose! Paper disproves Spock")
        print()

    elif playerchoice == "spock" and computerchoice == 3:
        print("Yeah! You win, Spock smashes Scissors")
        print('''👍''')
        print()
        score += 1

    elif playerchoice == "spock" and computerchoice == 4:
        print("You lose! Lizard poisons Spock")
        print()

    elif playerchoice == "spock" and computerchoice == 5:
        print("It's a tie!")
        print()

    if not input("play again? (y/n): ").lower() == "y":
        running = False

print("Thank you", str(name) + " for playing! you won " + str(score) + " times")
