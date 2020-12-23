# This is our first python script
# import a library with extra math operations
from math import *
import Modules
'''
First we learn how to print something to the terminal
with the print() built-in function
'''
print("----------------------------------\n"
      "Hello World\nWelcome to Python\n"
      "-----------------------------------")

# the escape character \n sends us to the next line
# we use backslash to print special characters " \ etc
print("Here we are gonna print a triangle\n"
      "   /|\n  / |\n /  |\n/___|"
      "\n-----------------------------------")

# here we store a string for later use
character_name = "George"

# here we store an int number for later use
character_age = 70
# to call a string variable in a string we use +
print("There once was a man named " + character_name + ",")

# to call a number variable in a string we use ,
print("he was ", character_age, " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being ", character_age, "")

# here we change the stored value of a variable
character_name = "Tom"

# here we store a float number for later use
character_height = 1.98

# number values can also be stored as strings
character2_age = "70"
print("\nHe had a friend named " + character_name + ",")
print("he was also " + character2_age + " years old")
print("and he was ", character_height, "meters tall")
print("-----------------------------------")
test_string = "Let's get started with our Tutorial"

# some functions to experiment with strings
# var.split(char) splits the words the char creates in a list
# var.strip() gets rid of the whitespaces at end and start
# strip(char) gets rid pff the char
print(test_string)
print(test_string.upper())
print(test_string.lower())
print(test_string.isupper())
print(test_string.upper().isupper())
print("The length of te test string is:", len(test_string))
print("Take specific characters:", test_string[0], ",", test_string[9], ",", test_string[13])
print("The word get starts in character", test_string.index("get"), "of the string")
print(test_string.replace("started", "done"))

# experimenting with numbers
print("\n-----------------------------------")
print("some numbers", 2, 4, 5)
print("3+4 =", 3 + 4)
print("3.45+4 =", 3.45 + 4)
print("3*4 =", 3 * 4)
print("5*3+4 =", 5 * 3 + 4)
print("5*(3+4) =", 5 * (3 + 4))
print("10/3 =", 10//3)
print("-10/3 =", -10//3)
print("10/3 =", 10 / 3)
num = 4
num += 5
print("4+5=", num)
print("10/3 div and mod", divmod(10, 3))
print("10/3 gives a module:", 10 % 3)
print("the absolute value of -5 is:", abs(-5))
print("3 raised to the power of 2:", pow(3, 2))
print("2^3 =", 2**3)
print("the highest number between 3,4,7,19 is:", max(3, 4, 7, 19))
print("the lowest number between 3,4,7,19 is:", min(3, 4, 7, 19))
print("3.14 rounded to one decimal", round(3.14, 1))
print("For 3.14 the floor is:", floor(3.14),
      "and the ceiling is:", ceil(3.14))
print("the square root of 100 is:", sqrt(100))
print(str(3) + " is a number as a string")
print("\n-----------------------------------")

# Now lets get user input
user_name = input("Enter your name:")
# the input function gets a string as value
# use float() or int()
user_age = int(input("Enter your age:"))
print("Hello " + user_name + " !\nSo you are ", user_age, " years old...")
print("_____________________________________________")
print("I printed this in 2 ", end=" one ")
print("prints without new line")
print("_____________________________________________")

text = """This is a multilined text
stored in a single string variable"""
print(text)
print("_____________________________________________")

print(Modules.my_variable)
print("The answer is:", Modules.multiply())
