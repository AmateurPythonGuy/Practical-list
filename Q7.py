# WAP to Read a text file line by line and display each word separated by #.

try: 
    file = open(r"sample.txt","r")

    for line in file.readlines():
        for word in line.split():
            print(word, end=" # ")
    
    file.close()
except FileNotFoundError:
    print("File not found")