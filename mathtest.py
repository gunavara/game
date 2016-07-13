import MySQLdb
db = MySQLdb.connect("localhost", "root", "osiris", "game")
cursor = db.cursor()

cursor.execute("SELECT health_points FROM players")

data = cursor.fetchall()

print int(data[1][0])

health_points = 20
user_search = "Guni"


cursor.execute("SELECT * FROM players")
updatehp = "UPDATE players SET health_points=%s WHERE username='%s'" % (health_points, user_search)

cursor.execute(updatehp)
db.commit()


