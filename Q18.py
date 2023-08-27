# WAP that generates random number between 1 and 6 which simulates dice.

from random import randint

while True:
    print("Would you like to roll the dice?")
    func = input("(y/n): ").lower()

    if func == "n":
        quit()
    else:
        print(randint(1,6))