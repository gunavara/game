import random


names = ["Dark Ancestor", "Volatile Ember", "Young dragon"]
enemy_name = (random.choice(names))


class Monster(object):
    def __init__(self, monster_name="", health_points=25, min_damage=1, max_damage=3, min_block=1, max_block=4):
        self.monster_name = monster_name
        self.health_points = health_points
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.min_block = min_block
        self.max_block = max_block
        self.enemy_name = enemy_name

    def enemy(self):
        print "Your enemy: " + enemy_name
        print "Health: " + str(self.health_points) + "\nDamage: " + str(self.min_damage) + " - " + str(self.max_damage) +"\nBlock: "+ str(self.min_block) + " - " + str(self.max_block)

    def createenemy(self):
        enemy1 = Monster()
        enemy1.enemy()


#monster1 = Monster(monster_name=enemy_name)
#monster1.enemy()

