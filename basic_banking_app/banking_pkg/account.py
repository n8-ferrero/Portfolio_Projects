'''ATM Program Function Definitions
by Nathanael Ferrero
11/11/2023
'''
# function to allow the user to view the account balance


def show_balance(balance):
    '''used to show current balance'''
    print(f"Your current balance is ${balance:,.2f}")

# function to allow the user to enter a deposit to their account


def deposit(balance):
    '''used to show the deposit options for the account'''
    money_in = input("Enter amount to deposit: $")
    return float(balance) + float(money_in)


# function to enter a withdrawl and update the account balance
def withdraw(balance):
    '''used to show the withdraw options for the account'''
    money_out = input("Enter amount to withdraw: $")
    # checks to see if the account has sufficient funds and subtracts withdrawl from balance
    if float(money_out) <= float(balance):
        return float(balance) - float(money_out)
    # if the withdrawl exceeds available funds, restricts the withdrawl
    elif float(money_out) > float(balance):
        print("Insufficient Funds.\nPlease select a different amount to withdraw")
        return float(balance)

# funtion to allow the user to log out


def logout(name):
    '''used to allow the user to exit the program and log out'''
    print(f"Goodbye {name}")
