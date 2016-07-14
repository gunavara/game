import mysql.connector

config = {
  'user': 'root',
  'password': 'guni123',
  'host': 'localhost',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = "SELECT id, username, user_address, user_age FROM users"

cursor.execute(query)

result_set = cursor.fetchall()
for row in result_set:
    print "%s, %s, %s, %s" % (row[0], row[1], row[2], row[3])
    print "------------------"
    print row[3]
    newone = int(row[3]) + 10
    print newone

cursor.close()
cnx.close()