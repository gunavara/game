import monsters
import heroclass
from random import randint
import start
import os


def clear():
    os.system('cls')


def lines():
    print "=========================="

roll = randint(1, 10)


def combat():
    first_enemy = monsters.Monster().createenemy()
    lines()
    heroclass.Warrior.attack(enemy_name=start.player1)


def startofquest1():
    print "Welcome to the forest of Dark Earth..."
    print "As you walk by a small set of rocks, right next to the path, you see an enemy!"

    runaway = raw_input("Would you try and runaway from the monster? Y/N\n> ")

    if runaway == "y":
        print "You roll the dice.. To successfully run away from the enemy, you need to roll 7 or more!"
        print "You roll: " + str(roll)
        if roll >= 7:
            print "You run away from the enemy without getting harmed."
        else:
            print "The enemy sees you and now there is no other option but to fight!"

    elif runaway == "n":
        clear()
        lines()
        print "It's time to fight!"
        lines()
        combat()

