
from random import randint
import os
import combat


import time


def clear():
    os.system('cls')


def sleep():
    time.sleep(1.5)


def lines():
    print "=========================="


def startofquest1():
    roll = randint(1, 10)
    clear()
    print "Welcome to the forest of Dark Earth..."
    print "As you walk by a small pile of rocks, right next to the path, you see an enemy!"

    runaway = raw_input("Would you try and runaway from the monster? Y/N\n> ")

    if runaway == "y":
        print "You roll the dice.. To successfully run away from the enemy, you need to roll 7 or more!"
        print "You roll: " + str(roll)
        if roll >= 7:
            print "You ran away from the enemy without getting harmed."
        else:
            print "The enemy sees you and now there is no other option but to fight!"
            combat.combat()
    elif runaway == "n":
        clear()
        lines()
        print "It's time to fight!"
        lines()
        combat.combat()



