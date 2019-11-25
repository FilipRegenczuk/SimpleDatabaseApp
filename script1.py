import sqlite3

connection = sqlite3.connect("lite.db")     # Connection to database lite.db
cursor = connection.cursor()
cursor.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
connection.commit()
connection.close()