import random    
import os   

os.system('cls')    #just using this to clear the screen when the code is run

def dice_game():
    
    high_score = 0    #set high score to zero 
    
    while True:
        #this will print out the current high score and the play options
        print(f"Current High Score: {high_score} \n 1) Roll Dice \n 2) Leave Game")
        #takes input on what the user wants to do
        play_input = input("Enter your choice: ")  
        #checks input '1' to run code
        if (play_input == "1"): 
            #randomizes two dice rolls
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            #adds those two rolls together
            total = dice1 + dice2
            #just printing this to space things out
            print("---------")
            #f string to print each dice roll and the current roll total
            print(f"You rolled a... {dice1} \nYou rolled a... {dice2} \nYour roll total is: {total}")
            #checking to see if the new roll is the high score. if yes, then the high score is reset
            #to the new total score
            if total > high_score:
                high_score = total
                print("---------")
                print("New High Score!")
                print("---------")
        #checking in play_input is '2' to exit program
        elif (play_input == "2"):
            print("Goodbye!")
            break
dice_game()