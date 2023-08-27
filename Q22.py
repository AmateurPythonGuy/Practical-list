# WAP to connect with database, delete a record and then display

import mysql.connector as mys

db = mys.connect(host="localhost", user="root", passwd="root", database="cs")
c = db.cursor()

if db.is_connected():
    print("Connected")
    iD = int(input("Enter admission ID of student: "))

    c.execute(f"delete from student where ADMIN_NO={iD}")
    db.commit()

    c.execute("select * from student")
    print([i for i in c.fetchall()])
else:
    print("Error")
    quit()

