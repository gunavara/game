import mysql.connector
import os
import quests
import time
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
            quests.startofquest1()
    else:
        print "Wrong selection, Goodbye."
# ---------------------END OF DASHBOARD + SAVED GAMES---------------------


# ---------------------REGISTRATION MODULE---------------------
def registration():

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
    register_player = "INSERT INTO players (username, hero_class, health_points, hero_min_dmg, hero_max_dmg, hero_min_block, hero_max_block) " \
                      "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (username, hero_class_selection, ss.starter_health, ss.starter_hero_min_dmg, ss.starter_hero_max_dmg, ss.starter_hero_min_block, ss.starter_hero_max_block)
    clear()
    lines()
    print "Congratulations, %s! You are now a level 1 %s. You have:\n%s health\nDamage: %s - %s\nBlock: %s - %s " %(username, hero_class_selection, ss.starter_health, ss.starter_hero_min_dmg, ss.starter_hero_max_dmg, ss.starter_hero_min_block, ss.starter_hero_max_block)
    lines()
    cursor.execute(register_player)
    cnx.commit()
    print "Starting your first quest..."
    sleep()
    quests.startofquest1()
# ---------------------END OF REGISTRATION MODULE---------------------

# ---------------------*****************************START OF PROGRAM*****************************---------------------
loading_screen()

# ---------------------END OF PROGRAM AND CLOSING DATABASE---------------------
cursor.close()
cnx.close()
raw_input()