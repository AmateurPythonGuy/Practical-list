# WAP to create a CSV file and store empno, name, salary, and search any empno and display name and salary, and if not found display appropriate message
import csv
data = []

n = int(input("Enter number of records: "))

for i in range(n):
    empno = int(input("Enter employee number: "))
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))

    data.append([empno, name, salary])

with open("fila.csv","w+") as f:
    w = csv.writer(f)
    w.writerows(data)

    f.seek(0)

    r = csv.reader(f)
    records = [i for i in r if i != []]

print(records)

while True:
    search = int(input("Enter employee number to be searched: "))
    for i in records:
        if str(search) == i[0]:
            print(i)
            break
    else:
        print("Invalid Employee Number")
    
    det = input("Continue? Y/N: ").upper()
    if det == "N":
        quit()
