# Write a menu driven program to perform insert,update and display on student binary file
from pickle import *

def insertRec():
    try:
        with open("file.dat",'rb') as f:
            data = load(f)
    except:
        data = []

    print("="*5,"Insert Record(s)","="*5,"\n")
    n = int(input("Enter number of requried records: "))
    for i in range(n):
        adminNo = int(input("Enter admission number: "))
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))

    data.append([adminNo, name, marks])

    with open("file.dat","wb") as f:
        dump(data, f)

def updateRec():
    temp = []
    try:
        with open("file.dat",'rb') as f:
            data = load(f)
    except:
        data = []
    
    if data == []: 
        print("Enter some data first")
    else:
        print("="*5,"Update Record","="*5,"\n")
        adminNo = int(input("Enter admission number: "))
        
        for i in data:
            if adminNo == i[0]:
                print("1. Name \n2. Marks")
                func1 = int(input("What would you like to change?: "))
                value = input("Enter value: ")

                if func1 == 1:
                    i[1] = value
                elif func1 == 2:
                    i[2] = int(value)
                else:
                    print("Why? Just why?")
                temp.append(i)
            else:
                temp.append(i)
        
        with open("file.dat","wb") as f:
            dump(temp, f)
                

def displayRecs():
    try:
        with open("file.dat",'rb') as f:
            data = load(f)
    except:
        data = []
    
    print([i for i in data])


while True:
    print("1. Insert record \n2. Update record \n3. Display records \n0. Quit")
    func = int(input("Enter function: "))

    if func == 0:
        quit()
    elif func == 1:
        insertRec()
    elif func == 2:
        updateRec()
    elif func == 3:
        displayRecs()