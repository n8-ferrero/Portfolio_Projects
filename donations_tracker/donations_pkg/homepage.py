#prints the menu to the screen.
def show_homepage():
    '''used to print the menu for 
    the user interface of the website'''
    print("")
    print("                                        ")
    print("      === DonateMe Homepage ===      ")
    print("----------------------------------------")
    print("|  1. Login       |  2. Register       |")
    print("----------------------------------------")
    print("|  3. Donate      |  4. Show Donations |")
    print("----------------------------------------")
    print("|              5. Exit                 |")
    print("----------------------------------------")

#functionality for the donation portion of the website.
def donate(username):
    '''this function is used to ask for a donation amount. It will then print a message to 
    the screen showing the current username and donation amount, and then return the 
    donations_string variable to be used to display all donations made'''
    donation_amt = float(input("Enter amount to donate: $"))
    donations_string = f"{username} donated ${donation_amt:,.2f}"
    print(f"{donations_string}! Thank you!")
    return donations_string

#functionality to allow a logged in user to view all donations.
def show_donations(donations):
    '''this will show all donations made. It will return a message if no donations have been made'''
    print("\n-------- All Donations --------")
    for x in donations:
        print(x)
    if len(donations) == 0:
        print("Sorry, there are no donations currently")
