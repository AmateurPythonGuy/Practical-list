# Write a program to read the content of file line by line and write to another file except for lines containing letter ‘a’.
try:
    with open("sample.txt","r") as file1:
        lines = file1.readlines()
        
    with open("sample2.txt","w") as file2:
        final = ""
        for i in lines:
            if "a" not in i:
                final += i
        file2.write(final)
except FileNotFoundError:
    print("File(s) does not exist")
