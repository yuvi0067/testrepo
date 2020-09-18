import random

print("DICE SIMULATOR:")
print("Press y and enter to roll the dice again.")
print("To exit press n and enter.")

x = "y"

while x == "y":

    n = random.randint(1,6)
    if n == 1:
        print("")
        print(" --------- ")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print(" --------- ")
    if n == 2:
        print("")
        print(" --------- ")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print(" --------- ")
    if n == 3:
        print("")
        print(" --------- ")
        print("|       O |")
        print("|    O    |")
        print("| O       |")
        print(" --------- ")
    if n == 4:
        print("")
        print(" --------- ")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print(" --------- ")
    if n == 5:
        print("")
        print(" --------- ")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print(" --------- ")
    if n == 6:
        print("")
        print(" --------- ")
        print("|  O   O  |")
        print("|  O   O  |")
        print("|  O   O  |")
        print(" --------- ")
    print("\n")
    x = input("y or n: ")
