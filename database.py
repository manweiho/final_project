import sqlite3

conn = sqlite3.connect('/home/ubuntu/week13_flask/employees.db')
print("Opened database successfully")

conn.execute('CREATE TABLE employees (EmpID TEXT, EmpName TEXT, EmpGender TEXT, EmpPhone TEXT, EmpBdate TEXT)')
print("Table created successfully")


conn.close(
