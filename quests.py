import monsters
from random import randint
import os
import starterstats as ss
import time

def clear():
    os.system('cls')

def sleep():
    time.sleep(1.5)

def lines():
    print "=========================="


def fight():
    first_enemy = monsters.Monster().createenemy()

    while ss.starter_health > 0:
        sleep()
        attack_roll = randint(1, 3)

        starter_block_roll = randint(ss.starter_hero_min_block, ss.starter_hero_max_block)

        successful_block_health_change = int(attack_roll) - int(starter_block_roll)

        roll = randint(1, 10)
        lines()
        print "Your enemy hits you for: %s" % attack_roll
        print "To block, you need to roll 7 or more! You roll: %s" % roll
        if roll >= 7:

            print "Successful block! You blocked: %s damage." % starter_block_roll
            print "Your enemy hits you for %s" %  successful_block_health_change
            ss.starter_health -= successful_block_health_change
            print "You now have: '%s' health left." % ss.starter_health
            lines()
        else:
            print "You couldn't block the enemy's attack!"
            print "Enemy hits you for: %s" % attack_roll
            ss.starter_health -= attack_roll
            print "You now have %s health" % ss.starter_health
            lines()

        print "Your turn to hit the enemy!"

        

        if ss.starter_health <= 0:
            print "You are dead. Sorry."
            lines()



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
            fight()
    elif runaway == "n":
        clear()
        lines()
        print "It's time to fight!"
        lines()
        fight()

