'''
Battle game 
by Nate Ferrero
Creation Date: 11/4/2023
'''

import os
os.system('cls')

WIZARD = "Wizard"
ELF = "Elf"
HUMAN = "Human"
ORC = "Orc"

CHARACTER = ()
MY_HP = ()
MY_DAMAGE = ()

WIZARD_HP = 70
WIZARD_DAMAGE = 150

ELF_HP = 100
ELF_DAMAGE = 100

HUMAN_HP = 150
HUMAN_DAMAGE = 20

ORC_HP = 200
ORC_DAMAGE = 85

DRAGON_HP = 300
DRAGON_DAMAGE = 50

while True:

    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    print("4) Orc")

    NUM = input("Please select your character: ")

    if NUM == "1":
        CHARACTER = WIZARD
        MY_HP = WIZARD_HP
        MY_DAMAGE = WIZARD_DAMAGE
        print()
        print("You selected the " + WIZARD)
        break
    elif NUM == "2":
        CHARACTER = ELF
        MY_HP = ELF_HP
        MY_DAMAGE = ELF_DAMAGE
        print()
        print("You selected the " + ELF)
        break
    elif NUM == "3":
        CHARACTER = HUMAN
        MY_HP = HUMAN_HP
        MY_DAMAGE = HUMAN_DAMAGE
        print()
        print("You selected the " + HUMAN)
        break
    elif NUM == "4":
        CHARACTER = ORC
        MY_HP = ORC_HP
        MY_DAMAGE = ORC_DAMAGE
        print()
        print("You selected the " + ORC)
        break
    else:
        print("Invalid Selection")

print("Your health is currently " + str(MY_HP))
print("Your damage output is " + str(MY_DAMAGE))
print()
print("------ Battle The Dragon ------")
print()

while True:

    print("You attack!")
    DRAGON_HP = DRAGON_HP - MY_DAMAGE
    if DRAGON_HP < 0:
       DRAGON_HP = 0
    print("The dragon now has " + str(DRAGON_HP) + " health remaining")
    if DRAGON_HP == 0:
        print("Congratulations, but our princess is in another castle!")
        break
    print()
    print("-------")
    print()
    print("The dragon retaliates!")
    print()
    MY_HP = MY_HP - DRAGON_DAMAGE
    if MY_HP < 0:
       MY_HP = 0
    print("--------")
    print()
    print("You now have " + str(MY_HP) + " heatlh remaining")
    print()
    if MY_HP == 0:
        print("Game over! Maybe you should try some fire-proof armor next time...")
        break
    else:
        print("The battle rages on!")
