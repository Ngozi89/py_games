# Import the module
import random


#Welcome message, game rules and player name
print("Welcome to game world")

player = input("Do you want to play Rock, Paper, Scissors game? ")

if player.lower() != "yes":
    quit()
else:
    print("Here is the rules for the game ")  
    print(" . There are 5 choices to chose (Fire, Wave, Fish, Boat, Grass)")
    print()
    print(" . You chose one and computer chose one")
    print()
    print(" . If your choice is same as the computer, you lose.")
    print()
    print(" . If your choice beats computer chose, you wine if not you lose")
    print()

player = input(" . If you are ready, type 'ok' ")

if player.lower() != "ok":
    quit()
else:
    print("Okay, lets' go :)")
print()   
# Let player enter name
name = input("Enter your name ").capitalize()
"Name: "
print("Hi,", str(name) + "!")
#End player name