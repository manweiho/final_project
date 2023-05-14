import mysql.connector as sql

conn = sql.connect(host="localhost", user="final", password="2807")
cur = conn.cursor()

# Test connection
print(conn)

cmd = "CREATE DATABASE flights_db"
cur.execute(cmd)
conn.close()
