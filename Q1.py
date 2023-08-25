# Write a menu-driven program to check for palindrome and armstrong.

while True:
    print("1. Check for palindrome\n2. Check Armstrong number\n0. Quit")
    func = int(input("Enter function: "))

    if func == 0:
       break
    elif func == 1:
        s = input("Enter string: ").lower()
        sRev = s[::-1]

        if sRev == s:
            print("Palindrome")
        else:
            print("Not palindrome")
    elif func == 2:
        sum_ = 0
        n = input("Enter number: ")
        exp = len(n)

        for i in range(exp):
            sum_ += int(n[i])**exp
        
        if sum_ == int(n):
            print("Armstrong number")
        else:
            print("not armstrong number")
