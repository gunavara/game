import mysql.connector
import os
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


def proceed():
    raw_input("Continue? (y/n)\n> ")

# ----------------------------- QUESTS ----------------------------
def startofquest1():
    print "Welcome to the forest of Dark Earth..."
    print "As you walk by a small pile of rocks, right next to the path, you see an enemy!"
    runaway()

def startofquest2():
    # =============== DICE ROLL GAME
    def dice_roll_game():

        player_dice_roll1 = randint(1, 10)
        andoar_dice_roll1 = randint(1, 10)
        player_dice_roll2 = randint(1, 10)
        andoar_dice_roll2 = randint(1, 10)
        player_dice_roll3 = randint(1, 10)
        andoar_dice_roll3 = randint(1, 10)
        player_total = 0
        andoar_total = 0
        lines()
        print "First roll: "
        print "You roll: %s" % player_dice_roll1
        print "Andoar rolls: %s" % andoar_dice_roll1
        player_total += player_dice_roll1
        andoar_total += andoar_dice_roll1
        lines()
        print "Second roll: "
        print "You roll: %s" % player_dice_roll2
        print "Andoar rolls: %s" % andoar_dice_roll2
        player_total += player_dice_roll2
        andoar_total += andoar_dice_roll2
        lines()
        print "Third roll: "
        print "You roll: %s" % player_dice_roll3
        print "Andoar rolls: %s" % andoar_dice_roll3
        player_total += player_dice_roll3
        andoar_total += andoar_dice_roll3
        lines()
        print "Your final score: %s" % player_total
        print "Andoar's final score: %s" % andoar_total
        if player_total > andoar_total:
            print "You won!"
            global dice_reward
            dice_reward = True

        elif player_total < andoar_total:
            print "You lost!"
            dice_reward = False
        else:
            print "It's a draw! You will roll until one of you rolls more than the other!"
            while player_total == andoar_total:
                you_roll = randint(1, 10)
                andoar_roll = randint(1, 10)
                print "You roll: %s" % you_roll
                print "Andoar rolls: %s " % andoar_roll
                if you_roll > andoar_roll:
                    print "You've won!"
                else:
                    print "You've lost!"
    # =============== END OF DICE ROLL GAME
    clear()
    print "After that fight you feel tired. You fell asleep for a while."
    print "After you wake up, you see an old man staring at you. He asks who are you and what are you doing here."
    lines()
    print "What do you say? (Enter the number corresponding to your answer)"
    print "1. Who I am is non of your business, old man!\n2. Why are you asking? And who are you?\n3. I am an adventurer in search of the black castle! Do you know where can I find it?"
    answer_choice = raw_input("> ")
    if answer_choice == "1" or answer_choice == "2":
        clear()
        print "The old man says: I am high mage Andoar and you are as stupid as you are brave. I will have to teach you a lesson in respect!"
    elif answer_choice == "3":
        clear()
        print "The old man says: I am high mage Andoar. I've been cast out from the realm and I try to leave peacefully my remaining days on this earth.\nYou look like an " \
              "adventurer who can use some wisdom and training. Do you want to train with me?"
        training_choice = raw_input("1. Train with the high mage\n2. No thanks.\n> ")
        if training_choice == "1":
            clear()
            print "Your training will begin shortly."
            lines()
            print "High mage Andoar says: I will teach you a lesson of chance. Gaining favor from the Arch powers is very important."
            print "We will play a game of chance and if you win, you will gain the favor of the Arch powers, thus giving you the ability to critically hit!"
            print "We will both roll the dice three times. Whoever rolls more in total, wins."
            dice_roll_game()
            if dice_reward == True:
                print "You have now learned the CRITICAL STRIKE abaility(passive)"
            elif dice_reward == False:
                print "TUKA SA TRQBVA DA GO IZMISLIME KVO STAVA LULULULULULL xD"
        elif training_choice == "2":
            print "Your choice, young adventurer. I hope you find what you are looking for. Goodbye."

    else:
        print "Wrong selection. Bye."


# ---------------------DASHBOARD + SAVED GAMES---------------------


# THE GAME STARTS HERE
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
        global user_search
        user_search = raw_input("Your name(case-sensitive)\n> ")

        query = "SELECT username, hero_class, health_points FROM players WHERE username='%s'" % user_search
        cursor.execute(query)
        clear()
        print "Welcome back!"
        lines()
        for (username, hero_class, health_points) in cursor:
            print "Player: %s\nClass: %s\nHealth: %s" % (username, hero_class, health_points)
            print "Starting your quest..."

            player_one = "SELECT queststage FROM players WHERE username='%s'" % user_search

            cursor.execute(player_one)
            player_one_stats = cursor.fetchall()
            for row in player_one_stats:
                stage = int(row[0])
                if stage == 1:
                    print "Starting quest 1." # <------------------------ START OF QUEST 1 IF QUEST STAGE == 1
                    sleep()
                    startofquest1()
                elif stage == 2:
                    print "Starting quest 2." # <------------------------ START OF QUEST 2 IF QUEST STAGE == 2
                    startofquest2()

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
    global user_search
    user_search = username

    sleep()
    startofquest1()

# ---------------------END OF REGISTRATION MODULE---------------------

# ----------------------COMBAT, RUNAWAY MODULE AND LOOT----------------------------------


def runaway():
    runaway_roll = randint(1,10)
    runaway = raw_input("Would you try and runaway from the monster? Y/N\n> ")
    if runaway == "y":
        print "You roll the dice.. To successfully run away from the enemy, you need to roll 7 or more!"
        print "You roll: " + str(runaway_roll)
        if runaway_roll >= 7:
            print "You ran away from the enemy without getting harmed."
        else:
            print "The enemy sees you and now there is no other option but to fight!"
            combat()
    elif runaway == "n":
        clear()
        lines()
        print "It's time to fight!"
        combat()

# COMBAT
def combat():

    def sleep():
        time.sleep(3)

    def clear():
        os.system('cls')

    def lines():
        print "=========================="

    player = user_search
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
                newxp = int(p1xp) + 10
                break

            lines()

            enemy_damage_hit = randint(nm.el1dmg_min, nm.el1dmg_max)
            print "Your enemy hits you for: %s" % enemy_damage_hit
            p1health = p1health - enemy_damage_hit
            print "You now have %s health points" % p1health
            sleep()
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
            sleep()
            if nm.el1hp <= 0:
                lines()
                print "You've won the fight!"
                lines()
                print "You've gained 10 xp"
                newxp = int(p1xp) + 10
                break

            if p1health <= 0:
                print "You died"

    if p1health > 0:
        victorious = True
    print "You have %s health points left after the fight" % p1health
    print "Continue? (y/n)"
    raw_input("> ")

    # UPDATE DATABASE STATS FOR PLAYER 1 ============================================================================
    player_one_update = "UPDATE players SET health_points='%s', player_xp='%s'," \
                        "queststage='2' WHERE username='%s'" % (p1health, newxp, user_search)
    cursor.execute(player_one_update)
    cnx.commit()
    # UPDATE DATABASE STATS FOR PLAYER 1 ============================================================================


    # VIEW NEW STATS AFTER FIGHT
    if victorious:
        def new_stats():
            clear()
            view_new_player_stats = "SELECT username, hero_class, health_points, hero_min_dmg, hero_max_dmg, hero_min_block, hero_max_block, player_xp FROM players WHERE username='%s'" % user_search
            cursor.execute(view_new_player_stats)
            new = cursor.fetchall()
            for row in new:
                playername = row[0]
                playerclass = row[1]
                playerhp = int(row[2])
                playermindmg = int(row[3])
                playermaxdmg = int(row[4])
                playerminblk = int(row[5])
                playermaxblk = int(row[6])
                playerxp = int(row[7])

            print "Your stats after the fight:"
            print "%s - %s" %(playername, playerclass)
            print "Health: %s" % playerhp
            print "Damage: %s - %s" %(playermindmg, playermaxdmg)
            print "Player block: %s - %s" % (playerminblk, playermaxblk)
            print "Player XP: %s" % playerxp
            time.sleep(5)
            proceed()
            startofquest2()
        # ENDOF VIEW NEW STATS AFTER FIGHT

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

            player_loot_upgrade = "UPDATE players SET hero_min_dmg='%s', hero_max_dmg='%s', hero_min_block='%s'," \
                                    " hero_max_block='%s' WHERE username='%s'" % (p1mindmg, p1maxdmg, p1minblk, p1maxblk, user_search)
            cursor.execute(player_loot_upgrade)
            cnx.commit()
            new_stats()

        else:
            clear()
            print "You've rolled less than 6."
            print "You did not find any loot."
            proceed()
            new_stats()


    cursor.close()
#----------------------COMBAT MODULE AND LOOT----------------------------------
loading_screen()
raw_input()