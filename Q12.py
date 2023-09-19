# Create a binary file with roll number, name and marks. Input a roll number and update the marks.
from pickle import * 

total = []
with open("sample.dat","wb") as f:
    n = int(input("Enter number of records: "))
    for i in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        mark = int(input("Enter marks: "))

        record = [roll, name, mark]
        total.append(record)
    print(total)

    dump(total, f)

with open("sample.dat",'rb') as f:
    table = load(f)

    updateRoll = int(input("Enter roll number to be updated: "))

    for roll, name, marks in table:
        if roll == updateRoll:
            value = int(input("Enter new marks: "))

            marks = value
            print([roll, name, marks])
            break
    else:
        print("Record not found")