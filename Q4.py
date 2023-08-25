# WAP to pass a string to a function and count occurrence of each vowels in it.
def countVowels(string):
    a, e, i, o, u = 0, 0, 0, 0, 0

    for x in string.lower():
        if x == 'a': a += 1
        elif x == 'e': e += 1
        elif x == 'i': i += 1
        elif x == 'o': o += 1
        elif x == 'u': u += 1
    
    return [a, e, i, o, u]

s = input("Enter string: ")
count = countVowels(s)

print(f"Number of vowels: \na={count[0]} \ne={count[1]} \ni={count[2]} \no={count[3]} \nu={count[4]}")