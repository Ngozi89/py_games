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

# Add player and computer choice
options = ("fire", "wave", "fish", "boat", "grass")
playerchoice = None
computerchoice = random.choice(options) #Computer choses randomly

while playerchoice not in options: # Keep runing until player chose from optionlist
    playerchoice = input("Make a choice (Fire, Wave, Fish, Boat, Grass) ").lower()

if playerchoice == "fire":
    print('''You chose '''+playerchoice+'''!''') #Print player choice
    print('''⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "wave":
    print('''You chose '''+playerchoice+'''!''') #Print player choice
    print('''⢠⠦⠴⠂⠒⠲⠙⠒⠶⠤⢄⡀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⠀⠀⠀
⠀⠀⠈⣧⠀⠀⠀⠀⣀⢄⣶⣿⣿⣷⣦⡄⠀⠀⠀⠈⡄⠀⠀
⠀⠀⠀⠑⠒⠓⠒⠋⠁⠀⠀⠘⣿⠙⢹⣷⣦⣀⠀⠀⠙⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠸⣿⣿⣿⣾⣇⠀⢄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣇⠸⣿⣿⢻⣿⡄⠸⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠟⠙⡀⣿⠛⢰⢻⡇⠐⡅
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⡞⠀⢰⣿⣿⡃⣼⣿⣿⢧⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⢠⣿⡾⣹⣽⠉⣧⣿⡎⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣮⢂⣾⡿⣃⠃⠃⣸⣿⡾⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡾⡡⣱⣿⢯⣾⣿⢯⢏⣾⣷⢯⡿⠁⠀⠀
⠀⢀⣀⣤⠶⠟⡩⣾⣴⡿⢗⣽⢟⠏⣼⣽⣿⣷⠟⠀⠀⠀⠀
⠉⠙⠫⠠⠔⠮⠬⠽⠿⠴⣟⠅⠡⠾⠧⠿⠟⠁⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "fish":
    print('''You chose '''+playerchoice+'''!''') #Print player choice
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀
⠈⣿⣶⣤⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
⠀⢹⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⢸⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀
⠀⣿⣿⠿⠋⠁⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "boat":
    print('''You chose '''+playerchoice+'''!''') #Print player choice
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⣦⢤⡤⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣬⢿⡇⠀⣿⠬⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢡⠃⠀⢇⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣌⡎⣩⡉⡉⡉⢉⢉⠉⢣⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠤⠼⠼⠝⡸⠹⠿⠇⠇⠿⠸⠀⠘⠦⡀⠀⠀⠀⠀⠀
⢀⣠⣤⣤⣤⣤⣤⣎⣜⣁⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣦⣤⣤⣀⡀
⢸⡁⢹⣼⣯⡀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⡇
⠘⢦⣈⣶⡷⢂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣜⡾⠁
⠀⠘⢏⠉⠫⡉⠉⠁⠀⠐⠛⠛⠛⠛⠛⠛⠛⠛⠃⠈⠽⠯⠭⢭⣯⡟⠁⠀
⠀⠀⠈⠳⣄⡈⠒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠉⠉⠁⠀⠀⠀⠀⠀⠀
    ''')

if playerchoice == "grass":
    print('''You chose '''+playerchoice+'''!''') #Print player choice
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡇⠀⠀⡆⠀⠀⠀⠀⠀⢀⠀⠀⣼⣿⠀⠀⠀⢰⠀⠀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⢸⡇⠀⠀⣷⠀⠀⢠⠀⠀⣸⡀⠀⣿⣿⠀⠀⠀⣼⡇⠀⠀⣼⠀⠀⢠⡆⠀
⠀⠀⣼⡇⠀⠀⣿⡆⠀⣾⠀⠀⣿⡇⢀⣿⣿⠀⠀⠀⣿⣿⠀⢀⣿⡇⠀⢸⡇⠀
⠀⠀⣿⣇⠀⢠⣿⣧⢀⣿⠀⢰⣿⡇⢸⣿⣿⡇⠀⢠⣿⣿⡆⢸⣿⡇⠀⣿⣷⠀
⠀⢀⣿⣿⠀⢸⣿⣿⢸⣿⡄⣼⣿⣷⢸⣿⣿⣿⣀⣾⣿⣿⡇⣿⣿⣷⢰⣿⣿⠀
⠀⢸⣿⣿⡇⢸⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀
    ''')


computerchoice = random.randint(1,5) # List computer choice in number 1-5
if computerchoice == 1:
    print('''The computer chose fire!''') #print computer choice
    print('''⠀⠀⠀⠀⠀⠀⢱⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
    ''')

elif computerchoice == 2:
    print('''The computer chose wave!''')
    print('''⢠⠦⠴⠂⠒⠲⠙⠒⠶⠤⢄⡀⢀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢤⣀⠀⠀⠀
⠀⠀⠈⣧⠀⠀⠀⠀⣀⢄⣶⣿⣿⣷⣦⡄⠀⠀⠀⠈⡄⠀⠀
⠀⠀⠀⠑⠒⠓⠒⠋⠁⠀⠀⠘⣿⠙⢹⣷⣦⣀⠀⠀⠙⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠸⣿⣿⣿⣾⣇⠀⢄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣇⠸⣿⣿⢻⣿⡄⠸⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠟⠙⡀⣿⠛⢰⢻⡇⠐⡅
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣞⡞⠀⢰⣿⣿⡃⣼⣿⣿⢧⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⢀⢠⣿⡾⣹⣽⠉⣧⣿⡎⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣮⢂⣾⡿⣃⠃⠃⣸⣿⡾⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡾⡡⣱⣿⢯⣾⣿⢯⢏⣾⣷⢯⡿⠁⠀⠀
⠀⢀⣀⣤⠶⠟⡩⣾⣴⡿⢗⣽⢟⠏⣼⣽⣿⣷⠟⠀⠀⠀⠀
⠉⠙⠫⠠⠔⠮⠬⠽⠿⠴⣟⠅⠡⠾⠧⠿⠟⠁⠀⠀⠀⠀⠀
    ''')

elif computerchoice == 3:
    print('''The computer chose fish!''')
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⡀⠀⠀⠀⠀
⠈⣿⣶⣤⡀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀
⠀⢹⣿⣿⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀
⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀
⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
⠀⢸⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀
⠀⣿⣿⠿⠋⠁⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀
⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡿⠿⠟⠋⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif computerchoice == 4:
    print('''The computer chose boat!''')
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⣦⢤⡤⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡧⣬⢿⡇⠀⣿⠬⠿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢡⠃⠀⢇⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣌⡎⣩⡉⡉⡉⢉⢉⠉⢣⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠤⠼⠼⠝⡸⠹⠿⠇⠇⠿⠸⠀⠘⠦⡀⠀⠀⠀⠀⠀
⢀⣠⣤⣤⣤⣤⣤⣎⣜⣁⣀⣀⣁⣀⣀⣀⣀⣀⣀⣀⣀⣀⣙⣦⣤⣤⣀⡀
⢸⡁⢹⣼⣯⡀⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣿⡇
⠘⢦⣈⣶⡷⢂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣜⡾⠁
⠀⠘⢏⠉⠫⡉⠉⠁⠀⠐⠛⠛⠛⠛⠛⠛⠛⠛⠃⠈⠽⠯⠭⢭⣯⡟⠁⠀
⠀⠀⠈⠳⣄⡈⠒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠀⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠉⠉⠁⠀⠀⠀⠀⠀⠀
    ''')

elif computerchoice == 5:
    print('''The computer chose grass!''')
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡇⠀⠀⡆⠀⠀⠀⠀⠀⢀⠀⠀⣼⣿⠀⠀⠀⢰⠀⠀⠀⢀⡇⠀⠀⠀⠀
⠀⠀⢸⡇⠀⠀⣷⠀⠀⢠⠀⠀⣸⡀⠀⣿⣿⠀⠀⠀⣼⡇⠀⠀⣼⠀⠀⢠⡆⠀
⠀⠀⣼⡇⠀⠀⣿⡆⠀⣾⠀⠀⣿⡇⢀⣿⣿⠀⠀⠀⣿⣿⠀⢀⣿⡇⠀⢸⡇⠀
⠀⠀⣿⣇⠀⢠⣿⣧⢀⣿⠀⢰⣿⡇⢸⣿⣿⡇⠀⢠⣿⣿⡆⢸⣿⡇⠀⣿⣷⠀
⠀⢀⣿⣿⠀⢸⣿⣿⢸⣿⡄⣼⣿⣷⢸⣿⣿⣿⣀⣾⣿⣿⡇⣿⣿⣷⢰⣿⣿⠀
⠀⢸⣿⣿⡇⢸⣿⣿⣾⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⣿⣿⣿⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⠀
    ''')

# Add Winner condition
if playerchoice == "fire" and computerchoice == 1:
    print("You tied! Try again!")

elif playerchoice == "fire" and computerchoice == 2:
    print("You lost! Try again!")

elif playerchoice == "fire" and computerchoice == 3:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "fire" and computerchoice == 4:
    print("Oops! Try again!")

elif playerchoice == "fire" and computerchoice == 5:
    print("Yeah! you win")
    print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇
''')

#Wave
if playerchoice == "wave" and computerchoice == 1:
    print("You tied! Try again!")

elif playerchoice == "wave" and computerchoice == 2:
    print("You lost! Try again!")

elif playerchoice == "wave" and computerchoice == 3:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "wave" and computerchoice == 4:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "wave" and computerchoice == 5:
    print("Oops! try again")

#Fish
if playerchoice == "fish" and computerchoice == 1:
    print("You tied! Try again!")

elif playerchoice == "fish" and computerchoice == 2:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "fish" and computerchoice == 3:
    print("You lost! Try harder!")

elif playerchoice == "fish" and computerchoice == 4:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "fish" and computerchoice == 5:
    print("Oops! Try again!")

#Boat
if playerchoice == "boat" and computerchoice == 1:
    print("You tied! Try again!")

elif playerchoice == "boat" and computerchoice == 2:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "boat" and computerchoice == 3:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "boat" and computerchoice == 4:
    print("Oops! Try again!")

elif playerchoice == "boat" and computerchoice == 5:
    print("You lost! Try again!")

#Grass
if playerchoice == "grass" and computerchoice == 1:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "grass" and computerchoice == 2:
    print("You lost! Try again!")

elif playerchoice == "grass" and computerchoice == 3:
    print("You lost! Try harder!")

elif playerchoice == "grass" and computerchoice == 4:
    print("Yeah! you win")
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠒⢦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⢉⣽⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠋⢐⣾⣷⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠡⠤⣮⣿⣵⠆⠠⠤⣀⣀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠏⠀⠐⢾⣽⣛⠟⠚⠛⠓⠒⠈⠱⡄
⠀⣀⣀⣤⣀⣤⣄⠠⡜⠃⠀⢀⣀⣼⣿⣿⠿⢦⣶⣶⣦⣿⣿⡟
⣾⣿⣿⠻⢿⣿⡇⠀⢫⣣⡱⣾⡿⣿⣿⣿⣆⣄⢀⢉⡉⣩⣿⠀
⢻⢻⡿⡎⠀⠀⢇⣀⣬⣷⠉⠙⠉⠙⣻⣿⠙⠓⠛⠿⣿⣿⠟⠀
⢸⣄⠈⢧⠀⠀⠸⡀⢀⣿⣤⣀⠀⠀⣺⡟⠿⣶⢦⣦⣤⡿⠀⠀
⠀⢻⣷⣼⡄⠀⠀⢱⣿⡿⠿⠾⠷⣶⣿⣷⣦⣌⢉⣻⠏⠁⠀⠀
⠀⠀⢧⣿⣷⡤⠒⠓⠁⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠁⠀⠀⠀⠀
⠀⠀⠈⣚⡻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

elif playerchoice == "grass" and computerchoice == 5:
    print("You tied! Try again!")