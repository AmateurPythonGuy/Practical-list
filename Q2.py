# WAP to input numbers in the list and find sum of odd numbers and sum of even numbers in the list.

l = []
even = 0
odd = 0

n = int(input("Enter limit: "))
for i in range(n):
    e = int(input(f"Enter element {i+1}: "))
    l.append(e)
print(l)

for i in l:
    if i%2 == 0:
        even += i
    else:
        odd += i

print(f"Sum of: \nEVEN = {even}\nODD = {odd}")
