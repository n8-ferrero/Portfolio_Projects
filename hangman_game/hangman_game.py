'''word list slightly altered from the list located at
https://github.com/Xethron/Hangman/blob/master/words.txt

Hangman Game
written by Nathanael Ferrero
11/1/2023 - 11/29/2023
'''

from hangman_func import select_word
from hangman_func import guessed_input
from hangman_func import player_guesses
from hangman_func import guessed_word
from hangman_func import game_over_man
from hangman_func import clear_screen
from hangman_func import draw_the_hangman


clear_screen()          #calls the clear_screen function
print("Let's play HANGMAN! Please guess a letter")      #Welcome message

word = select_word()    #sets word to the randomly selected word from words.txt
guesses = set()         #sets guesses to a blank set at the beginning of the round
INCORRECT_GUESSES = 0   #sets incorrect_guesses to zero at the start of the round
CORRECT_WORD = guessed_word(word, guesses)  #sets correct_word to the guesses_word function

while not game_over_man(INCORRECT_GUESSES, word, guesses):
    draw_the_hangman(INCORRECT_GUESSES)     #draws the graphics using incorrect_guesses to determine appropriately
    print(f"Your word is: {CORRECT_WORD}")          #displays underlines and correct letters
    print(f"Guessed Letters: {player_guesses(guesses)}\n")  #displays all guessed letters

    player_guess = guessed_input(guesses)   #sets player_guess to the guessed_input function
    if player_guess in word:
        print("\nGood Guess!")        #message for successful guess 
    else:
        print("\nOuch, try again")    #message for incorrect guess
        INCORRECT_GUESSES += 1      #incremenet incorrect_guesses by 1 for each wrong guess

    guesses.add(player_guess)   #adds the guess to the guesses set for display on the screen
    CORRECT_WORD = guessed_word(word, guesses)  #updates display to include correct letters

draw_the_hangman(INCORRECT_GUESSES)     #calls the draw function
if INCORRECT_GUESSES == 7:                                #checks to determine how many incorrect guesses there are
    print("That's a tough loss. Please try again!")       #displays game over message if 7 incorrect guesses
else:
    print("Nice guessing!")                               #victory message
print(f"Your word was: {word}")                           #shows the word to the player
