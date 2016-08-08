import mysql.connector

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

# user_search = "Joro"

player_one = "SELECT queststage FROM players WHERE username='Joro'"

cursor.execute(player_one)
player_one_stats = cursor.fetchall()
for row in player_one_stats:
  stage = int(row[0])

if stage < 5:
    print stage
else:
    print "Higher than 5"



view_new_player_stats = "SELECT username, hero_class, health_points, hero_min_dmg, hero_max_dmg, hero_min_block, hero_max_block FROM players WHERE username='jojo'"
cursor.execute(view_new_player_stats)
player_new_stats = cursor.fetchall()
for row in player_new_stats:
    user_name = row[0]
print user_name

