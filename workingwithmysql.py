import mysql.connector

config = {
  'user': 'root',
  'password': 'guni123',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def registration():
    print "Register a new user"
    username = raw_input("Name: ")
    password = raw_input("Password: ")

    class Employee(object):
        def __init__(self, employee_name="", employee_password=""):
            self.employee_name = employee_name
            self.employee_password = employee_password

        def putindb(self):

            self.employee_name = username

            self.employee_password = password

            add = "INSERT INTO users (username, password) VALUES ('%s', '%s')" % (username, password)
            cursor.execute(add)
            cnx.commit()

    user = Employee(employee_name=username, employee_password=password)
    user.putindb()

    qry = "SELECT id, username, password FROM users"
    cursor.execute(qry)
    for (id, username, password) in cursor:
        print "ID: {}".format(id)
        print "-----------------------------"
        print "USER: {}".format(username)
        print "-----------------------------"
        print "PASS: {}".format(password)
        print "-----------------------------"

registration()
cursor.close()
cnx.close()
