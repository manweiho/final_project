import sqlite3

conn = sqlite3.connect('/home/ubuntu/final_project/flights.db')
print("Opened database successfully")

conn.execute('CREATE TABLE flights (FLIGHTID INT AUTO_INCREMENT PRIMARY KEY, FirstName TEXT, LastName TEXT, Email TEXT, Phone TEXT, Origins TEXT, Destination TEXT, Date DATE)')
print("Table created successfully")

conn.close(
