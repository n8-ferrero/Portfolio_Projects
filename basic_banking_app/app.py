'''ATM Program
by Nathanael Ferrero
11/11/2023
'''
# import account because it has all of the calculation information
from banking_pkg.account import show_balance, deposit, withdraw, logout

# setting the variables to zero
balance = 0


# this is the atm menu that will appear for the user
def atm_menu(name):
    '''shows the menu for the ATM'''
    print("")
    print("     === Automated Teller Machine ===     ")
    print("             User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


# This will allow a user to create an account
print("     === Automated Teller Machine ===     ")

while True:
    name = input("Enter name to register: ")
    pin = input("Enter PIN: ")
    # used to set limits for the username and pin number
    if len(name) <= 10 and len(pin) == 4:
        break
    if len(name) > 10 and len(pin) == 4:
        print("Username must be 10 or fewer characters")
    elif len(name) <= 10 and len(pin) > 4:
        print("Pin value must be 4 characters long")
    elif len(name) > 10 and len(pin) > 4:
        print("Username must be 10 or fewer characters\n and pin must be 4 characters long")
    elif len(name) <= 10 and len(pin) < 4:
        print("PIN must be exactly 4 characters long")

# this just states that a user account was created and shows the starting balance
print(f"{name} has been registered with a starting balance of ${balance}")

# while loop to check the user login against the registered user
while True:
    print("     === USER LOGIN ===     ")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    # checks user name and pin and gives appropriate error messages if wrong
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful")
        break
    if name_to_validate == name and pin_to_validate != pin:
        print("Invalid Pin!")
    elif name_to_validate != name and pin_to_validate == pin:
        print("Invalid Username!")
    elif name_to_validate != name and pin_to_validate != pin:
        print("All credentials are invalid")

# while loop to check user input and run the functions from account
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif option == "3":
        balance = withdraw(balance)
        show_balance(balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Please check your selection again")
