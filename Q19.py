# WAP to connect with database and add multiple records in student table
# fields are: (admission number,name,gender,mark,stream)

import mysql.connector as mys

db = mys.connect(host="localhost", user="root", passwd="root", database="cs")
c = db.cursor()

if db.is_connected():
    print("Connected")
else:
    print("Error")
    quit()

def insert():
    iD = int(input("Enter id: "))
    name = input("Enter name: ")
    gender = input("Enter gender (M/F): ")
    mark = int(input("Enter marks: "))
    stream = input("Enter stream: ")

    c.execute(f"insert into student values ({iD},'{name}', '{gender}', {mark}, '{stream}')")
    db.commit()

while True:
    print("1. Add record \n0. Quit")
    func = int(input("Enter function: "))
    if func == 0:
        db.close()
        c.close()
        break
    elif func == 1:
        insert()
    else:
        print("Stop doing this")