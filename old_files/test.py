import monsters
from random import randint
import os
import starterstats as ss
def lines():
    print "=========================="

attack_roll = randint(10, 20)

starter_block_roll = randint(ss.starter_hero_min_block, ss.starter_hero_max_block)

successful_block_health_change = starter_block_roll - attack_roll

unsuccessful_block_health_change = ss.starter_health - attack_roll

roll = randint(1, 10)

first_enemy = monsters.Monster().createenemy()


while ss.starter_health > 0:
        lines()
        print ss.starter_health
        print "Enemy hits you for: %s" % attack_roll
        print "You now have %s health" % unsuccessful_block_health_change
        ss.starter_health -= attack_roll
