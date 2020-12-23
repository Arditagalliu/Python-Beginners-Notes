# r only read if file doesn't exist is an error
# a only appends or creates the file
# w writes in file or creates the file
# x creates the file or displays error
file = open("text.txt", "r")

print("Is the file readable?", file.readable())
print("______________________________________")
print("This is the content of the file:")
print("______________________________________")
print(file.read())
print("______________________________________")
file.close()

second_file = open("text.txt", "r")

print(second_file.readline(), end="")
print(second_file.readline(), end="")
print("______________________________________")
print(second_file.read())

second_file.close()

file = open("text.txt", "r")

print("______________________________________")
for row in file.readlines():
    print(row, end=".")
print("\n______________________________________")

file.close()

file = open("text.txt", "a")

file.write("\nThis is a new line")

file.close()
'''
file = open("text.txt", "w")

file.write("This is the only line")

file.close()

file = open("index.html", "w")

file.write("<h1>This is the only line</h1>")

file.close()
'''
