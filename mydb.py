import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234'
)

cursor = database.cursor()
cursor.execute("CREATE DATABASE stocks")
print("Done")