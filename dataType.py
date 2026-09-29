#Data Types in Python
# In Python, data types are used to define the type of data that a variable can hold. Python has several built-in data types, including:
# 1. Numeric Types: int, float, complex
# 2. Text Type: str
# 3. Boolean Type: bool
# 4. Sequence Types: list, tuple, range
# 5. Mapping Type: dict
# 6. Set Types: set, frozenset
# 7. Binary Types: bytes, bytearray, memoryview

# Example of different data types:
# Integer variable
age = 25  # int
# Float variable
height = 5.9  # float
# Complex variable
complex_num = 3 + 4j  # complex
# String variable
name = "John"  # str
# Boolean variable
is_student = True  # bool
# List variable
fruits = ["apple", "banana", "cherry"]  # list
# Tuple variable
coordinates = (1, 2, 3)  # tuple
# Range variable
numbers = range(1, 10)  # range
# Dictionary variable
person = {"name": "Alice", "age": 30, "city": "New York"}  # dict
# Set variable
unique_numbers = {1, 2, 3, 4, 5}  # set
# Frozen Set variable
frozen_unique_numbers = frozenset({1, 2, 3, 4, 5})  # frozenset
# Bytes variable
data = b"Hello"  # bytes
# Bytearray variable
data_array = bytearray(b"Hello")  # bytearray
# Memoryview variable
data_view = memoryview(b"Hello")  # memoryview

#We dont need to declare the data type of a variable explicitly in Python. The interpreter automatically infers the data type based on the value assigned to the variable. However, you can use the type() function to check the data type of a variable.

#To check the data type of a variable, you can use the type() function. For example:
print(type(age))  # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(complex_num))  # Output: <class 'complex'>
print(type(name))  # Output: <class 'str'>
print(type(is_student))  # Output: <class 'bool'>
print(type(fruits))  # Output: <class 'list'>
print(type(coordinates))  # Output: <class 'tuple'>
print(type(numbers))  # Output: <class 'range'>
print(type(person))  # Output: <class 'dict'>
print(type(unique_numbers))  # Output: <class 'set'>
print(type(frozen_unique_numbers))  # Output: <class 'frozenset'>
print(type(data))  # Output: <class 'bytes'>
print(type(data_array))  # Output: <class 'bytearray'>
print(type(data_view))  # Output: <class 'memoryview'>