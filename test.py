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
user_search = "Guni"

'''
query = "SELECT username, hero_class, health_points FROM players WHERE username='%s'" % user_search
cursor.execute(query)
for (username, hero_class, health_points) in cursor:
    print "Player: %s\nClass: %s\nHealth: %s" % (username, hero_class, health_points)

hp_after_dmg = 93

updatehp = "UPDATE players SET health_points=%s WHERE username='%s'" % (hp_after_dmg, user_search)
cursor.execute(updatehp)

hp_before_dmg = ""

viewhp_before_dmg = "SELECT health_points FROM players WHERE username='Guni'"
cursor.execute(viewhp_before_dmg)
for (health_points) in cursor:
    print "HP: %s" % health_points


health_points = 25
updatehp = "UPDATE players SET health_points=%s WHERE username='%s'" % (health_points, user_search)
cursor.execute(updatehp)
print "-----------------------------------"
for (health_points) in cursor:
    print "HP: %s" % health_points

'''
damage = 10
viewhp_before_dmg = "SELECT health_points FROM players WHERE username='Guni'"
cursor.execute(viewhp_before_dmg)



#new_health_points = health_points - 5

#updatehp = "UPDATE players SET health_points=%s WHERE username='%s'" % (new_health_points, user_search)
#cursor.execute(updatehp)
print "-----------------------------------"
for (health_points) in cursor:
    print int(health_points[0][1])



cnx.commit()

cursor.close()
cnx.close()
