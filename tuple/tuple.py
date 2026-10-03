# Tuples in python
# Tuples are a collection of ordered, immutable elements. They are similar to lists, but unlike lists, tuples cannot be changed after their creation. Tuples are defined by enclosing the elements in parentheses `()`.

# Declaration of a tuple
my_tuple = (1, 2, 3, 4, 5)

print("Tuple:", my_tuple)
print("Second element:", my_tuple[1])  # Accessing the second element
print("Last element:", my_tuple[-1])  # Accessing the last element
print("First element:", my_tuple[0])  # Accessing the first element

# Mixing data types in a tuple
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# Type of the tuple
print("Type of my_tuple:", type(my_tuple))  
print("Type of mixed_tuple:", type(mixed_tuple)) #output: <class 'tuple'>

# to declare 1 element tuple we need to add a comma after the element
single_element_tuple = (1,)
print("Single element tuple:", single_element_tuple)
print("Type of single_element_tuple:", type(single_element_tuple)) #output: <class 'tuple'>

# converting a list to a tuple
my_list = [1, 2, 3, 4, 5]
my_tuple_from_list = tuple(my_list)
print("Tuple from list:", my_tuple_from_list)
print("Type of single_element_tuple:", type(single_element_tuple)) #output: <class 'tuple'>

# converting a tuple to a list
my_list_from_tuple = list(my_tuple)
print("List from tuple:", my_list_from_tuple)
print("Type of my_list_from_tuple:", type(my_list_from_tuple)) #output: <class 'list'>

# Slicing a tuple
print("First three elements:", my_tuple[0:3])
print("Elements from index 1 to 3:", my_tuple[1:4])

# Immutable nature of tuples
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e) #output: Error: 'tuple' object does not support item assignment

# Tuple is immutable, but if it contains mutable elements like lists, those elements can be modified.
tuple_with_list = (1, 2, [3, 4])

# Methods of tuple
# Tuples have only two built-in methods: count() and index().
print("Count of 2 in tuple_with_list:", tuple_with_list.count(2))
print("Index of 2 in tuple_with_list:", tuple_with_list.index(2))

# Modifying the list inside the tuple
tuple_with_list[2].append(5)
print("Tuple with modified list:", tuple_with_list)

# Tuple unpacking
a, b, c = tuple_with_list
print("Unpacked values:", a, b, c)
