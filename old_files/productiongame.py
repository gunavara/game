import mysql.connector
import os
import quests
import time
import monsters_and_loot as nm
from random import randint
# ---------------------DATABASE CONNECTION AND INVOKE + CURSOR CREATION---------------------


config = {
  'user': 'root',
  'password': 'guni123',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
# ---------------------END OF DATABASE CONNECTION AND INVOKE + CURSOR CREATION---------------------


def sleep():
    time.sleep(3)


def clear():
    os.system('cls')


def lines():
    print "=========================="


# ---------------------DASHBOARD + SAVED GAMES---------------------

def loading_screen():
    lines()
    print "Welcome to Guni Quest v0.1"
    lines()
    print "1. Start a new game\n2. Continue where you left"
    loading_screen_selection = raw_input("> ")
    if loading_screen_selection == "1":
        registration()
    elif loading_screen_selection == "2":
        print "Loading..."
        print "Available saved games:"
        list_of_players = "SELECT username FROM players"
        cursor.execute(list_of_players)
        for (user) in cursor:
            lines()
            print "User: %s" % user

        user_search = raw_input("Your name(case-sensitive)\n> ")
        query = "SELECT username, hero_class, health_points FROM players WHERE username='%s'" % user_search
        cursor.execute(query)
        clear()
        print "Welcome back!"
        lines()
        for (username, hero_class, health_points) in cursor:
            print "Player: %s\nClass: %s\nHealth: %s" % (username, hero_class, health_points)
            print "Starting your quest..."
            sleep()

            quest_stage_check = "SELECT queststage FROM players WHERE username='%s'" % user_search
            cursor.execute(quest_stage_check)
            cursor.fetchall()
            for row in quest_stage_check:
                current_stage = row[0]
                if current_stage == 1:
                    print "Starting your first quest!"

    else:
        print "Wrong selection, Goodbye."
# ---------------------END OF DASHBOARD + SAVED GAMES---------------------


# ---------------------REGISTRATION MODULE---------------------
def registration():
    starter_health = 100
    starter_hero_min_dmg = 1
    starter_hero_max_dmg = 3
    starter_hero_min_block = 2
    starter_hero_max_block = 4
    starter_quest_stage = 1
    starter_xp = 0

    print "Please enter your username: "
    username = raw_input("> ")
    print "Please select a hero class!\n1. Warrior\n2. Mage\n3. Druid"
    hero_class_selection = raw_input("> ")
    if hero_class_selection == "1":
        hero_class_selection = "Warrior"
    elif hero_class_selection == "2":
        hero_class_selection = "Mage"
    elif hero_class_selection == "3":
        hero_class_selection = "Druid"
    register_player = "INSERT INTO players (username, hero_class, health_points, hero_min_dmg, hero_max_dmg, " \
                      "hero_min_block, hero_max_block, player_xp, queststage) " \
                      "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
                      % (username, hero_class_selection,
                         starter_health, starter_hero_min_dmg,
                         starter_hero_max_dmg,
                         starter_hero_min_block,
                         starter_hero_max_block, starter_xp,
                         starter_quest_stage)
    clear()
    lines()
    print "Congratulations, %s! You are now a level 1 %s. You have:\n%s health\nDamage: %s - %s\nBlock: %s - %s " \
          "\nExperience: %s" \
          % (username, hero_class_selection, starter_health, starter_hero_min_dmg, starter_hero_max_dmg,
             starter_hero_min_block, starter_hero_max_block, starter_xp)
    lines()
    cursor.execute(register_player)
    cnx.commit()
    print "Starting your first quest..."
    sleep()
    startofquest1()

# ---------------------END OF REGISTRATION MODULE---------------------


# ----------------------COMBAT MODULE AND LOOT----------------------------------
def combat():

    def sleep():
        time.sleep(3)

    def clear():
        os.system('cls')

    def lines():
        print "=========================="

    player = loading_screen().user_search
    player_one = "SELECT username, hero_class, health_points, hero_min_dmg, hero_max_dmg, hero_min_block," \
                 " hero_max_block, player_xp FROM players WHERE username='%s'" % player

    cursor.execute(player_one)
    player_one_stats = cursor.fetchall()
    for row in player_one_stats:
        p1name = row[0]
        p1class = row[1]
        p1health = int(row[2])
        p1mindmg = int(row[3])
        p1maxdmg = int(row[4])
        p1minblk = int(row[5])
        p1maxblk = int(row[6])
        p1xp = int(row[7])

    print p1name, "-", p1class
    print "Health: %s\nDamage: %s - %s\nBlock: %s - %s\nExperience: %s" % (p1health, p1mindmg, p1maxdmg, p1minblk, p1maxblk, p1xp)

    lines()

    print "Enemy: %s" % nm.enemy_name_level_one
    nm.el1statsinfo()
    lines()
    print "Rolling for first hit..."
    sleep()
    first_hit_roll_p1 = randint(1, 10)
    first_hit_roll_enemy = randint(1, 10)
    lines()

    print "You roll: %s" % str(first_hit_roll_p1)
    print "Enemy rolls: %s" % str(first_hit_roll_enemy)

    if first_hit_roll_p1 > first_hit_roll_enemy:  # IF **YOU** HIT FIRST
        print "You will hit first!"

        while p1health > 0:
            player_one_damage_hit = randint(p1mindmg, p1maxdmg)
            print "You hit your enemy for %s" % player_one_damage_hit
            nm.el1hp -= player_one_damage_hit
            print "Your enemy now has %s health points" % nm.el1hp
            if nm.el1hp <= 0:
                lines()
                print "You've won the fight!"
                lines()
                print "You've gained 10 xp"
                newxp = p1xp + 10
                break

            lines()

            enemy_damage_hit = randint(nm.el1dmg_min, nm.el1dmg_max)
            print "Your enemy hits you for: %s" % enemy_damage_hit
            p1health = p1health - enemy_damage_hit
            print "You now have %s health points" % p1health

            if p1health <= 0:
                print "You died"

    elif first_hit_roll_p1 <= first_hit_roll_enemy: # IF **ENEMY** HISTS FIRST
        print "Your enemy will hit first!"
        while p1health > 0:
            enemy_damage_hit = randint(nm.el1dmg_min, nm.el1dmg_max)
            print "Your enemy hits you for: %s" % enemy_damage_hit
            p1health = p1health - enemy_damage_hit
            print "You now have %s health points" % p1health

            lines()

            player_one_damage_hit = randint(p1mindmg, p1maxdmg)
            print "You hit your enemy for %s" % player_one_damage_hit
            nm.el1hp -= player_one_damage_hit
            print "Your enemy now has %s health points" % nm.el1hp
            if nm.el1hp <= 0:
                lines()
                print "You've won the fight!"
                lines()
                print "You've gained 10 xp"
                newxp = p1xp + 10
                break

            if p1health <= 0:
                print "You died"

    if p1health > 0:
        victorious = True
    print "You have %s health points left after the fight" % p1health

    # UPDATE DATABASE STATS FOR PLAYER 1 ============================================================================
    player_one_update = "UPDATE players SET health_points='%s', player_xp='%s'," \
                        "queststage='2' WHERE id='1'" % (p1health, newxp)
    cursor.execute(player_one_update)
    cnx.commit()
    # UPDATE DATABASE STATS FOR PLAYER 1 ============================================================================


    if victorious:
        print "You try and loot the corpse of your enemy. Rolling for success...(you must roll 6 or more to find loot)"
        lootroll = randint(0, 10)
        print lootroll
        if lootroll >= 6:
            print "You found loot!"
            print "You loot: %s" % nm.quest1_loot

            if nm.quest1_loot == nm.sword1:
                p1mindmg = p1mindmg + nm.sword1_min
                p1maxdmg = p1maxdmg + nm.sword1_max
            elif nm.quest1_loot == nm.axe1:
                p1mindmg = p1mindmg + nm.axe1_min
                p1maxdmg = p1maxdmg + nm.axe1_max
            elif nm.quest1_loot == nm.shield1:
                p1minblk = p1minblk + nm.shield1_min
                p1maxblk = p1maxblk + nm.shield1_max

            player_weapon_upgrade = "UPDATE players SET hero_min_dmg='%s', hero_max_dmg='%s', hero_min_block='%s'," \
                                    " hero_max_block='%s' WHERE id='1'" % (p1mindmg, p1maxdmg, p1minblk, p1maxblk)
            cursor.execute(player_weapon_upgrade)
            cnx.commit()

        else:
            print "You've rolled less than 6."
            print "You did not find any loot."
    cursor.close()
#----------------------COMBAT MODULE AND LOOT----------------------------------



# ---------------------*****************************START OF PROGRAM*****************************---------------------
loading_screen()

# ---------------------END OF PROGRAM AND CLOSING DATABASE---------------------

raw_input()
