import sqlite3

conn = sqlite3.connect('/home/ubuntu/final_project/flights.db')
print("Opened database successfully")

conn.execute('CREATE TABLE employees (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate TEXT)')
print("Table created successfully")


conn.close(
