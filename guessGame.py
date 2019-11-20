import random
import time
import platform
import os

def clr_scr():
    if platform.system() == "Windows":
        print("\n\n.......Clearing Screen..........\n\n")
        time.sleep(2)
        os.system('cls')
    else : 
        print("\n\n.......Clearing Screen..........\n\n")
        time.sleep(2)
        os.system('clear')
        
def guessGame():
    clr_scr()
    comGuess = random.randint(1,50)
    print("\n\nGuess a number between 1 to 50.")
    chance = 5 
    while chance != 0 : 
        print(f"\n\n!!!You have Left {chance} to win this game!!!\n\n")
        userGuess = int(input(f"Your Guess[{6-chance}]: "))
        if userGuess < 1 or userGuess > 50:
            print("\nWarning!!!! Your guess out of limit...Guess Between 1-50")
            continue
        if userGuess == comGuess:
            print("\n\nWhola!!! You such a master player")
            print("\nYeah!!!!!!You have Won The Game!!!!!")
            time.sleep(5)
            clr_scr()
            break
        elif userGuess > comGuess:
            print("\nHint!!!Be in Limits Think Lower")
        else : 
            print("\nHint!!!Be Big Think Big")
        chance -= 1

    else : 
        print(f"\n\nComputer Guess was : {comGuess}")
        print("\nHee haa hee haaa haaa!!! You Such a Looser")
        time.sleep(5)
        clr_scr()

        
clr_scr()     
while input("\n\n\t\tPress any key to play game and enter to exit : "):
       guessGame()
else : 
    print("\n\n\n\tBye Bye User From Guess Game\n\n\n")
    time.sleep(5)
    clr_scr()
