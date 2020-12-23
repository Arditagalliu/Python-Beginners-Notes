contact_list = ["kevin", "Karen", "James", "Nicolas", "Toby"]
abstract_list = ["John", 3, "Someone", True]
abs1, abs2, abs3, abs4 = abstract_list
print("Unpacking a list and printing the third element: ", abs3)
numbers_list = [4, 8, 15, 16, 23, 42]

# Some simple list functions
print("all my contacts are:", contact_list)
print("the second contact is: ", contact_list[1])
print("the last contact is: ", contact_list[-1])
print("the contacts from the second and after are: ", contact_list[1:])
print("the contacts from the second to third are: ", contact_list[1:3])
print("the contacts up to the third are: ", contact_list[:3])

contact_list[2] = "Mike"
print("\nAll my contacts now are:\n", contact_list)

contact_list.append("Steve")
print("\nAll my contacts now are:\n", contact_list)

contact_list.insert(1, "Marry")
print("\nMy contacts after adding Marry to second place:\n", contact_list)

contact_list.remove("Mike")
print("\nMy contacts after removing Mike:\n", contact_list)

contact_list.pop()
print("\nMy contacts after removing the last:\n", contact_list)

abstract_list.extend(numbers_list)
print("\nAbstract_list after adding numbers_list:\n", abstract_list)

abstract_list.clear()
print("\nAbstract list after clear", abstract_list)

print("\nThe contact Karen is in:", contact_list.index("Karen") + 1)

contact_list.append("Marry")
print("\nThe contact Marry is ", contact_list.count("Marry"), "times")

contact_list.sort()
print("\nMy contacts after sorting:\n", contact_list)

contact_list.reverse()
print("\nMy contacts reversed:\n", contact_list)

abstract_list = contact_list.copy()
print("\nAbstract list after copy:\n", abstract_list)
print("______________________________________")

# tuples  cant be edited you just access them
coordinate_node = (4, 5)
print(coordinate_node[1])
print("______________________________________")

# we can have a list of tuples
coordinates_list = [(4, 5), (6, 7), (80, 34)]
print(coordinates_list)
print("______________________________________")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# we can have a 2-d list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(number_grid)
print(number_grid[1][2])
print("______________________________________")
# we can have a 3-d list
number_grid = [
    [[1.1, 1.2, 1.3], [2.1, 2.2, 2.3], [3.1, 3.2, 3.3]],
    [[4.1, 4.2, 4.3], [5.1, 5.2, 5.3], [6.1, 6.2, 6.3]],
    [[7.1, 7.2, 7.3], [8.1, 8.2, 8.3], [9.1, 9.2, 9.3]]
]
print(number_grid)
print(number_grid[2][2][1])
print("______________________________________")
