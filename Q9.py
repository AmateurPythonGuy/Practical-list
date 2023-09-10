# Write a program to read the content of file line by line and write to another file
# except for lines containing letter ‘a’.
try:
    file1 = open(r"sample1.txt","r")
    file2 = open(r"sample2.txt", "w")

    lines = file1.readlines()
    final = ""

    for i in lines:
        if "a" not in i:
            final += i

    file2.write(final)

    file1.close()
    file2.close()
except FileNotFoundError:
    print("File does not exist")