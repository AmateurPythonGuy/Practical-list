# WAP to connect with database and display records in student table.

import mysql.connector as mys

db = mys.connect(host="localhost", user="root", passwd="root", database="cs")
c = db.cursor()

if db.is_connected():
    print("Connected")
else:
    print("Error")
    quit()

c.execute("select * from student")
table = c.fetchall()

for i in table:
    print(i)