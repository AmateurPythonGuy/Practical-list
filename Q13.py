# WAP to write dictionary of names and phone numbers to binary file then search for a phone number using name.
from pickle import *

dlist = []

with open("sample.dat","wb") as f:
    n = int(input("Enter number of records: "))
    for i in range(n):
        d = dict()
        name = input("Enter name: ")
        phno = int(input("Enter phone number: "))

        d["Name"] = name ; d["Phno"] = phno
        dlist.append(d)
    
    dump(dlist, f)

with open("sample.dat","rb") as f:
    table = load(f)
    while True:
        searchPh = int(input("Enter phone number to be searched: "))

        for i in table:
            if i["Phno"] == searchPh:
                print(i["Name"])
                break
        else:
            print("Phone number not found")

        det = input("Continue(y/n): ")
        if det != "y":
            break