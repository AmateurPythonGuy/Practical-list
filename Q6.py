# WAP to input numbers in the list and perform linear and binary search.
l = []

n = int(input("Enter limit: "))
for i in range(n):
    e = int(input("Enter element: "))
    l.append(e)

print(l)


search = int(input("Enter element to be searched: "))

# linear
for i in l:
    if search == l:
        print(f"Element found at index: {l.index(search)}")
else:
    print("Nothing found :(")


searchB = int(input("Enter element to be searched: "))

# binary
right = len(l)-1
left = 0

while left <= right:
    mid = left + (right - left)//2

    if l[mid] == searchB:
        print(f"Element found at index: {mid}")
        break
    elif l[mid] < searchB:
        left = mid + 1
    else:
        right = mid - 1
else:   
    print("Element not found")