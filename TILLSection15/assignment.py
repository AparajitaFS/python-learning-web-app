# rate = 0.95
# dollars = float(input("How many dollars have you got: "))
# euros = dollars * rate
# print("The amount in euros is:")
# print(euros)

# ranking = ['John', 'Sen', 'Lisa']
# rank = int(input("Enter rank number: ")) - 1
# print(ranking[rank])

# ranking = ['John', 'Sen', 'Lisa']
# name = input("Enter a name: ")
# print(ranking.index(name)+1)


# filenames = ['document', 'report', 'presentation']
# for i, item in enumerate(filenames):
#     print(f"{i}-{item}.txt")

# ips = ['100.122.133.105', '100.122.133.111']
# i = int(input("Enter the index of the IP you want: "))-1
# print(f"You chose {ips[i]}")

# while True:
#     with open('sides.txt', 'r') as file:
#         sides = file.readlines()
#     side = input("Throw the coin and enter head or tail here: ?") + "\n"
#     sides.append(side)
#
#     with open('sides.txt', 'w') as file:
#         file.writelines(sides)
#
#     heads = sides.count('head\n')
#     percentage = heads / len(sides) * 100
#
#     print(f"Heads: {percentage}%")

# password = input("Enter a new password: ")
#
# if len(password) > 7:
#     print("Great password there!")
# elif len(password) == 7:
#     print("Password is OK, but not too strong")
# else:
#     print("Your password is weak.")

import csv
with open("data/city.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)