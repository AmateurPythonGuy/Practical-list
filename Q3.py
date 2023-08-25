# WAP to  input n numbers in tuple and pass it to function to count how many even and odd numbers are entered.

def count(tup):
    even = 0
    odd = 0
    for i in  tup:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
    
    return [even, odd]


t = tuple()
even = 0
odd = 0

n = int(input("Enter limit: "))
for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    t += (e,)
print(t)

c = count(t)
print(f"NUMBER OF: \nEVEN NUMBERS: {c[0]}\nODD NUMBERS = {c[1]}")