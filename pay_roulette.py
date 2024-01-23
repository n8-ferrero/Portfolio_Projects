import random

names_string = "Angela, Stanley, Michael, Pam, Kevin, Oscar, Creed, Andy, Jim, Phylis, Dwight, Toby, Ryan, Kelly, Karen, Gabe"
names = names_string.split(", ")

total_names = int(len(names))
pick_name = random.randint(0, total_names - 1)
lucky_number = names[pick_name]

print(f"{lucky_number} is going to buy the meal today!")
