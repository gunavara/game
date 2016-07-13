from random import randint


def  lines():
    print "----------------------"


class Warrior(object):
    def __init__(self, player_name="Player", type="Warrior", health_points=100, min_damage=1, max_damage=3, min_block=1, max_block=4):
        self.player_name = player_name
        self.type = type
        self.health_points = health_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.min_block = min_block
        self.max_block = max_block

    def printwarrior(self):
        print "Your name is: " + self.player_name + "\nYou are: " + self.type + "\nHealth: " + str(self.health_points) + "\nDamage: "\
              + str(self.min_damage) + " - " + str(self.max_damage) + \
              "\nBlock: " + str(self.min_block) + " - " + str(self.max_block)

    def remove_hp(self, dmg=0):
        self.health_points -= dmg
        lines()
        print "%s was hit for: " % self.player_name + str(dmg)
        lines()

    def attack(self, enemy_name=""):
        damagehit = randint(self.min_damage, self.max_damage)
        lines()
        print "%s hits %s for %s" % (self.player_name , enemy_name , str(damagehit))
        return damagehit



'''
player1 = Warrior(player_name="Guni")
player1.printwarrior()
player2 = Warrior(player_name="Dancho")
player2.printwarrior()
dmg = player2.attack(enemy_name=player1.player_name)
player1.remove_hp(dmg=dmg)

player1.printwarrior()
'''

