# WAP to perform push, pop, display stack containing book details(bookno, bookname, author)
stack = []

lim = int(input("Enter limit: "))

print(stack)

def add():
    no = int(input("Enter book number: "))
    name = input("Enter book name: ")
    auth = input("Enter author: ")
    
    stack.append([no, name, auth])

while True:
    print("1. Push \n2. Pop \n3. Peek \n4. Display \n0. Quit")
    func = int(input("Enter function: "))
    if func == 0:
        quit()
    elif func == 1:
        if len(stack) >= lim:
            print("Overflow")
        else:
            add()
    elif func == 2:
        try:
            stack.pop()
            print(stack)
        except IndexError:
            print("Underflow")
    elif func == 3:
        try:
            print(stack[-1])
        except IndexError:
            print("Empty stack")
    elif func == 4:
        try:
            print(stack[::-1])
        except IndexError:
            print("Empty stack")