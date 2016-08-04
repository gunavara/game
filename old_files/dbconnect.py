import mysql.connector


def connect():
    config = {
      'user': 'root',
      'password': 'osiris',
      'host': '127.0.0.1',
      'database': 'game',
      'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()


