import mysql.connector as sql

conn = sql.connect(host="localhost", user="final", password="2807", database="flights_db")
cur = conn.cursor()

cmd = "CREATE TABLE flights (\
    FlightID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    FirstName VARCHAR(30) NOT NULL,\
    LastName VARCHAR(30), \
    Email VARCHAR(30), \
    Phone VARCHAR(30),\
    Origin VARCHAR(30),\
    Destination VARCHAR(30),\
    Date DATE,\
    DepartureTime VARCHAR(30))"

cur.execute(cmd)
conn.close()
