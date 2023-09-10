# Read a text file and display the number of vowels/consonants/uppercase/lowercase
# characters in the file.

try: 
    file = open(r"sample.txt","r")
    data = file.read().replace("\n", "")

    up = 0; low = 0
    vow = 0; cons = 0

    for i in data:
        if i.lower() in ('a', 'e', 'i', 'o', 'u'):
            vow += 1
        else:
            cons += 1
        
        if i.isupper():
            up += 1
        else:
            low += 1

    print(f"[UPPER, lower]: {up, low}")
    print(f"[vowels, consonants]: {vow, cons}")
    file.close()
except FileNotFoundError:
    print("File not found")

