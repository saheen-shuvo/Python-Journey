# List in Python: A collection of items in a specific order.

# Creating a list
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
print(type(numbers))  # <class 'list'>

# Accessing elements in a list using indexing
first_element = numbers[0]  # 1
last_element = numbers[-1]  # 5
print(first_element)  # 1
print(last_element)  # 5

# Modifying elements in a list (mutable)
numbers[0] = 10
print(numbers)  # [10, 2, 3, 4, 5]

# Adding elements to a list
numbers.append(6)  # Adds 6 to the end of the list
print(numbers)  # [10, 2, 3, 4, 5, 6]

# Inserting elements at a specific index
numbers.insert(1, 15)  # Inserts 15 at index 1  
print(numbers)  # [10, 15, 2, 3, 4, 5, 6]

# Removing elements from a list
numbers.remove(3)  # Removes the first occurrence of 3
print(numbers)  # [10, 15, 2, 4, 5, 6]

# Popping elements from a list
popped_element = numbers.pop()  # Removes and returns the last element (6)
print(popped_element)  # 6
print(numbers)  # [10, 15, 2, 4, 5, 6]

# Slicing a list
sliced_list = numbers[1:4]  # [15, 2, 4]
print(sliced_list)  # [15, 2, 4]

# Iterating through a list
for num in numbers:
    print(num)  # Prints each number in the list

# List comprehension
squared_numbers = [x**2 for x in numbers]  # Creates a new list with the squares of the numbers
print(squared_numbers)  # [100, 225, 4, 16, 25, 36]

# Checking if an element exists in a list
exists = 15 in numbers  # True
print(exists)  # True

# Getting the length of a list
length_of_list = len(numbers)  # 6
print(length_of_list)  # 6

# Sorting a list (Ascending order)
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # [2, 4, 5, 10, 15]

# Sorting a list (Descending order)
numbers.sort(reverse=True)  # Sorts the list in descending order
print(numbers)  # [15, 10, 5, 4, 2]

# Copying a list
copied_list = numbers.copy()  # Creates a shallow copy of the list
print(copied_list)  # [15, 10, 5, 4, 2]

# Clearing a list
numbers.clear()  # Removes all elements from the list
print(numbers)  # []

# Nested lists (lists within lists)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
first_nested_element = nested_list[0][1]  # 2
print(first_nested_element)  # 2

# Modifying elements in a nested list
nested_list[0][1] = 20
print(nested_list)  # [[1, 20, 3], [4, 5, 6], [7, 8, 9]]

# List methods in Python:
# 1. append(): Adds an element to the end of the list.
# 2. extend(): Adds all elements from another iterable to the end of the list.
# 3. insert(): Inserts an element at a specific index.
# 4. remove(): Removes the first occurrence of an element.
# 5. pop(): Removes and returns the element at a specific index.
# 6. clear(): Removes all elements from the list.
# 7. index(): Returns the index of the first occurrence of an element.
# 8. count(): Returns the number of occurrences of an element.
# 9. sort(): Sorts the elements in ascending order.
# 10. reverse(): Reverses the order of the elements in the list.
# 11. copy(): Creates a shallow copy of the list.