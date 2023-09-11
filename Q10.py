# WAP to count the words ‘this’ and ‘that’ in text file
try:
    with open("sample.txt") as file:
        data = file.read().lower()
        print(f"Number of occurences of: \n[This, That] = {[data.count('this'), data.count('that')]}")
except FileNotFoundError:
    print("File does not exist")
