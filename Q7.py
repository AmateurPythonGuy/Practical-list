# WAP to Read a text file line by line and display each word separated by #.
try:
    with open("sample.txt") as file:
        for i in file.read().split():
            print(i, end=" # ")
except FileNotFoundError:
    print("File does not exist")
