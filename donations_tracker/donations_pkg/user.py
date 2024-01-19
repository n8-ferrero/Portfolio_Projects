#allows a user to log into the banking program
def login(database,username,password):
    '''this function will check to ensure the username is registered, and the supplied
    password is correct for the username supplied. If a username or password is incorrect, 
    it will simply reply with invalid credentials'''
    if username in database and password == database[username]:
        print(f"Welcome {username}!")
        return username
    elif username in database and password != database[username]:
        print("Invalid login credentials")
        return ""
    else:
        print("Invalid login credentials")
        return ""

#allows a user to register for the banking program
def register(database,username):
    '''this checks to see if the username being supplied is already registered. An error will
    be displayed if the username already exists. A confirmation will be displayed if the new
    username is successfully registered.'''
    if username in database:
        print("User already exists")
        return ""
    else:
        print(f"{username} registered!")
        return username
