switch_is_on = True
i = 1
while switch_is_on:
    if i == 10:
        print("It's closed")
        switch_is_on = False
    else:
        i += 1
        print("It's still on", i - 1)
print(i)
print("______________________________________")

i = 1
while i <= 3:
    print("Its smaller than 4: ", i)
    i += 1
else:
    print("Its not smaller than 3:", i)
print("______________________________________")

i = 1
while i <= 3:
    print("This is i: ", i)
    i += 1
print(i)
print("______________________________________")

numbers_list = [2, 4, 5, 2, 5, 8]
while 3 not in numbers_list:
    number = input("Please enter the number 3: ")
    numbers_list.append(int(number))
print(numbers_list)
print("______________________________________")

for letter in "Hello World":
    print(letter)
print("______________________________________")

names_list = ["John", "Marry", "Nick", "Peter"]
for name in names_list:
    print(name)
print("______________________________________")

for index in range(5):
    print("The number is: ", index)
print("______________________________________")

for index in range(2, 5):
    print("The number is: ", index)
print("______________________________________")

for index in range(len(names_list)):
    print("(", index + 1, ") " + names_list[index])
print("______________________________________")

for index in range(10):
    if index == 5:
        break
    print("The index is: ", index)
print("______________________________________")

for index in range(5):
    if index == 3:
        continue
    print("The index is: ", index)
print("______________________________________")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in number_grid:
    for collum in row:
        print(collum, end=" ")
    print("")
print("______________________________________")

for row in number_grid:
    for collum in row:
        if collum % 3 != 0:
            print(collum, end=" ")
        else:
            print(collum)
print("______________________________________")

try:
    number = int(input("Enter a number: "))
    print("The number is: ", number)
    print(number / 0)
except ValueError:
    print("Invalid number")
except ZeroDivisionError as err:
    print(err)
