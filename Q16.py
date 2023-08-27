# WAP to implement a stack(push,pop,peek,display) on the set of numbers.

stack = []

lim = int(input("Enter limit: "))

print(stack)

while True:
    print("1. Push \n2. Pop \n3. Peek \n4. Display \n0. Quit")
    func = int(input("Enter function: "))
    if func == 0:
        quit()
    elif func == 1:
        if len(stack) >= lim:
            print("Overflow")
        else:
            element = int(input("Enter element: "))
            stack.append(element)
            print(stack)
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
    else:
        print("You're not supposed to be here")