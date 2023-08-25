# WAP to find area and perimeter of different shapes (circle,rectangle,square) using user defined functions

class Area:
    def circle(radius):
        from math import pi
        return pi * radius * radius
    
    def square(side):
        return side * side
    
    def rectangle(length, breadth):
        return length * breadth

print("AREA CALCULATOR")
print("1. Circle \n2. Square \n3. Rectangle")
func = int(input("Enter shape: "))

if func == 1:
    r = int(input("Enter radius: "))
    print(Area.circle(r))
elif func == 2:
    s = int(input("Enter side: "))
    print(Area.square(s))
elif func == 3:
    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))
    print(Area.rectangle(length, breadth))
else:
    print("What are you doing here?")