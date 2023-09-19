# Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
from pickle import * 

total = []
with open("sample.dat","wb") as f:
    n = int(input("Enter number of records: "))
    for i in range(n):
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")

        record = [roll, name]
        total.append(record)
    print(total)

    dump(total, f)

with open("sample.dat","rb") as f:
    table = load(f)

    while True:
        search = int(input("Enter roll number: "))

        for roll, name in table:
            if search == roll:
                print([roll, name])
                break
        else:
            print("Record not found")
        
        det = input("Continue(y/n): ")
        if det != "y":
            break
