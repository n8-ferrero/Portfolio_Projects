from random import choice
import os

def clear_screen():
    """clear the console screen. A check has been implemented to determine if
    'cls' should be used for Windows, or 'clear' should be used for NIX based OSes"""
    os.system('cls' if os.name == "nt" else "clear")        
    #cls will work on Windows based OS, clear will work on UNIX based OS

def select_word():
    """select a random word from the words.txt file"""
    #this will open the words.txt file and set it as the variable file_open
    with open("words.txt", "r") as file_open:
        word_list = file_open.readlines()               #reads every line and returns the results as a string element
    return choice(word_list).strip()                #used to remove leading and trailing whitespace

def guessed_input(guesses):
    """gets input from the player, and validates the input is a letter
    Arguments: guesses (set) set of guessed letters
    Returns: valid letter input"""

    while True:
        player_input = input("Guess a letter: ").lower()        #gets input as lower case 
        #this will check to make sure the player input is a single alphabetic character that has not been guessed yet
        if len(player_input) == 1 and player_input.isalpha() and player_input not in guesses:
            return player_input

def player_guesses(guesses):
    """formats and joins the guessed letters for display on the screen in alphabetic order"""
    return " ".join(sorted(guesses))    

def guessed_word(word, guesses):
    """formats the word with guessed letters revealed and 
    all other missing letters as an underscore to allow
    the player to view how many letters are in the unknown word"""
    return " ".join([letter if letter in guesses else '_' for letter in word])

def game_over_man(incorrect_guesses, word, guesses):
    """checks to see if the game is over
    Arguments: number of incorrect guesses, the target word, and the set of guessed letters
    Returns: True if the game is over, False if not"""
    return incorrect_guesses == 7 or set(word) <= set(guesses)

def draw_the_hangman(incorrect_guesses):
    """draws the hangman based on how many incorrect guesses there are"""
    hangman = (
        r"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

        r"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

        r"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    H A""",

        r"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    H A N""",

        r"""
   _________             
    |/   |               
    |   (_)                   
    |  \_|_/                     
    |    |                    
    |                        
    |                          
    |___                          
    H A N G""",

        r"""
   _________              
    |/   |                     
    |   (_)                     
    |  \_|_/                    
    |    |                       
    |                             
    |                            
    |___                          
    H A N G M""",

        r"""
   ________                   
    |/   |                         
    |   (_)                      
    |  \_|_/                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    H A N G M A""",

        r"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    H A N G M A N""")

    print(hangman[incorrect_guesses])   #this draws the appropriate image using incorrect_guesses to determine which version to draw
