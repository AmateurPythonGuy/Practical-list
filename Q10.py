# WAP to count the words ‘this’ and ‘that’ in text file
try:
    file = open(r"sample.txt","r")

    data = file.read().lower()
    print(f"Number of this = {data.count('this')}")
    print(f"Number of the = {data.count('the')}")

    file.close()
except FileNotFoundError:
    print("File does not exist")