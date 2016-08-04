import mysql.connector
import os
import quests
import starterstats as ss
import time

config = {
  'user': 'root',
  'password': 'guni123',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def sleep():
    time.sleep(3)


def clear():
    os.system('cls')


def lines():
    print "=========================="


lines()


questprogressquery = "SELECT queststage FROM players WHERE id='1'"
cursor.execute(questprogressquery)
quest_stage = cursor.fetchall()

for row in quest_stage:
    print "You have completed level: %s" % row[0]
    stage = int(row[0])
    nextlevel = stage + 1
    print "Loading level: %s" % nextlevel


raw_input()
