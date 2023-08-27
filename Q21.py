# WAP to connect with database, search and update the records in student table.

import mysql.connector as mys

db = mys.connect(host="localhost", user="root", passwd="root", database="cs")
c = db.cursor()

if db.is_connected():
    print("Connected")
else:
    print("Error")
    quit()

def update(iD, column, val):
    if column == 1:
        c.execute(f"update student set NAME='{val}' where ADMIN_NO={iD}")
    elif column == 2:
        c.execute(f"update student set GENDER='{val}' where ADMIN_NO={iD}")
    elif column == 3:
        c.execute(f"update student set MARK={int(val)} where ADMIN_NO={iD}")
    elif column == 4:
        c.execute(f"update student set STREAM='{val}' where ADMIN_NO={iD}")
    
    db.commit()

while True:
    print("1. Update record \n2. Search record \n0. Quit")
    func = int(input("Enter function: "))
    if func == 0:
        quit()
    elif func == 1:
        iD = int(input("Enter admission ID of student: "))
        c.execute(f"select * from student where ADMIN_NO={iD}")

        print(c.fetchone())
        print("1. Name \n2. Gender (M/F)\n3. Mark\n4. Stream")

        func1 = int(input("What would you like to update? "))
        val = input("Enter new value: ")

        update(iD, func1, val)
    elif func == 2:
        iD = int(input("Enter admission ID of student: "))
        c.execute(f"select * from student where ADMIN_NO={iD}")
        print(c.fetchone())
    else:
        print("pls stop ur not funny")