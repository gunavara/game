import mysql.connector

# ---------------------DATABASE CONNECTION AND INVOKE + CURSOR CREATION---------------------


config = {
  'user': 'root',
  'password': 'osiris',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,

}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# user_search = "Joro"

list_of_players = "SELECT username FROM players"
cursor.execute(list_of_players)
for (user) in cursor:

    print "User: %s" % user

