# Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
try:
    with open("sample.txt") as file:
        upper = 0; lower = 0; vows = 0; cons = 0
        
        data = file.read().replace("\n","")

        for i in data:
            if i.lower() in ('a', 'e', 'i', 'o', 'u'):
                vows += 1
            else:
                cons += 1
            
            if i.isupper():
                upper += 1
            else:
                lower += 1
        
        print(f"[Vowels, Consonants, Uppercase, Lowercase] : {[vows, cons, upper, lower]}")
except FileNotFoundError:
    print("File does not exist")
