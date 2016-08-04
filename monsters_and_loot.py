import random


def lines():
    print "================================="

names_level_one = ["Dark Ancestor", "Volatile Ember", "Young dragon"]
names_level_two = [
    "Stonehound",
    "Grievefang",
    "Fogteeth",
    "Fetidlich",
    "The Fickle Miscreation",
    "The Disgusting Deformity",
    "The Infamous Body",
    "The Blind Cinder Serpent",
    "The Taloned Nightmare Pig",
    "The Golden Nightmare Bear"
]


# QUEST 1 ===============================================================
# ENEMY LEVEL 1 STATS
el1hp = 10
el1dmg_min = 1  # ENEMY LEVEL ONE DAMAGE MINIMUM
el1dmg_max = 3  # ENEMY LEVEL ONE DAMAGE MAXIMUM
el1blk_min = 1  # ENEMY LEVEL ONE BLOCK MINIMUM
el1blk_max = 4  # ENEMY LEVEL ONE BLOCK MAXIMUM

enemy_name_level_one = (random.choice(names_level_one))
lines()


def el1statsinfo():
    print "Health: %s" % el1hp
    print "Damage: %s - %s " % (el1dmg_min, el1dmg_max)
    print "Block: %s - %s" % (el1blk_min, el1blk_max)

# QUEST 1 LOOT
sword1 = "'Sword of the dragon' (2 - 4) dmg"
sword1_min = 2
sword1_max = 4
axe1 = "'Axe of the dragon' (1 - 3) dmg"
axe1_min = 1
axe1_max = 3
shield1 = "'Scale of the dragon' (1 - 1) block"
shield1_min = 1
shield1_max = 1

enemy_level_one_loot = [sword1, axe1 , shield1]
quest1_loot = (random.choice(enemy_level_one_loot))


# /QUEST 1 ===============================================================
