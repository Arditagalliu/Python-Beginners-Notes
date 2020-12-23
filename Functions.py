
def greeting(name):
    print("Welcome " + name)


def counter(surname):
    count = len(surname)
    return count


username = input("Whats your name ")
greeting(username)
user_surname = input("Whats your surname ")
print("Your surname has ", counter(user_surname), " letters")

if counter(user_surname) < 10:
    print("Your surname is small")

elif counter(user_surname) > 10:
    print("Your surname is long")

else:
    print("Your surname is medium")

is_male = True
is_female = False

if (is_male or is_female) and not(is_male and is_female):
    if is_male:
        print("you are male")

    else:
        print("you are female")

elif is_male and is_female:
    print("something is wrong you cant be both")


def find_max(num1, num2):
    if num1 > num2:
        return "the first"

    elif num2 > num1:
        return "the second"

    elif num1 == num2:
        return "none! they are equal"


number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))

print("The highest number is:" + find_max(number1, number2))

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("There is a banana in the fruits list")
else:
    print("There is not a banana in the fruits list")


def local_var():
    var = "This is local"
    print(var)


var = "This is global"
local_var()
print(var)


def local_var2():
    global var2
    var2 = "Now is global"
    print(var2)


var2 = "This is global"
local_var2()
print(var2)
