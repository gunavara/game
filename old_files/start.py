import os
import heroclass
import quests
import mysql.connector

config = {
  'user': 'root',
  'password': 'osiris',
  'host': '127.0.0.1',
  'database': 'game',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def exit():
    exit_choice = raw_input("Exit? Y/N > ")
    if exit_choice == "y":
        print "Goodbye."
    else:
        print "Ok."


def clear():
    os.system('cls')


def lines():
    print "=========================="


def combat():
    print "The combat is about to begin"
    print "Enemies: "

username = ""


def register():
    lines()
    print "Welcome to Guni Quest v0.1"
    lines()
    print "Please enter your username"
    username = raw_input("> ")
    insert_username = "INSERT INTO players (username) VALUES ('%s')" % username
    cursor.execute(insert_username)
    cnx.commit()
    clear()
    lines()
    print "Welcome " + username + "!"
    print "Let's select a class for your hero!"
    print "Available classes are:"
    lines()
    print "1. Warrior\n2. Mage\n3. Druid"
    hero_class_choice = raw_input("Select your hero: ")
    clear()
    if hero_class_choice == "1":
        hero_class_choice = "Warrior"
        '''
        insert_warrior = "INSERT INTO players (user_class) VALUES ('%s')" % hero_class_choice
        cursor.execute(insert_warrior)
        cnx.commit()
        '''
        player1 = heroclass.Warrior(player_name=username)
        clear()
        player1.printwarrior()
    elif hero_class_choice == "2":
        hero_class_choice = "Mage"
    elif hero_class_choice == "3":
        hero_class_choice = "Druid"
    print "Congratulations " + username + ". You are now a " + hero_class_choice
    lines()
    quests.startofquest1()
    lines()

register()

raw_input()
cursor.close()
cnx.close()