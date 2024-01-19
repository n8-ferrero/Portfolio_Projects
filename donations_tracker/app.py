'''DonateMe webpage exercise
by Nathanael Ferrero
11/18/2023'''

#import funtions to allow the code to properly function
from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

#declaring the global variables
database = {"admin": "password123"}
donations = []
authorized_user = ''

#while loop to check if a user is logged in, and to allow the full functionality of the program
while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as {authorized_user}")

    user_input = input("Choose an option: ")
    #takes user input to allow an existing user to log in.
    if user_input == "1":
        username = input("Please enter your username: ").lower()
        password = input("Please enter your password: ")
        authorized_user = login(database, username, password)
    #takes user input to allow a new user to register
    elif user_input == "2":
        username = input("Please register a username: ").lower()
        password = input("Please register a password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username]=password
    #takes user input to allow a donation.
    elif user_input == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donations_string = donate(authorized_user)
            donations.append(donations_string)
    #takes user input to show donations.
    elif user_input == "4":
        show_donations(donations)
    #takes user input to exit the program.
    elif user_input == "5":
        print("Thank you for using DonateMe. Goodbye!")
        break
    #shows error message if an invalid selection is made.
    else:
        print("Invalid Selection. Please choose a valid menu option.")