#Taking input from the user
name = input("Enter your name: ")
print("Hello, " + name)

#Type conversion
# In Python, you can convert data from one type to another using built-in functions. This process is called type conversion or type casting. Here are some common type conversion functions in Python:
# 1. int(): Converts a value to an integer.
# 2. float(): Converts a value to a float.
# 3. str(): Converts a value to a string.
# 4. bool(): Converts a value to a boolean.
# 5. list(): Converts a value to a list.
# 6. tuple(): Converts a value to a tuple.
# 7. set(): Converts a value to a set.
# 8. dict(): Converts a value to a dictionary.

# Example of type conversion:
# Converting a string to an integer
num_str = "10"
num_int = int(num_str)  # num_int will be 10 (integer)
print(num_int, type(num_int))  # Output: 10 <class 'int'>

# Converting a string to a float
num_str = "10.5"
num_float = float(num_str)  # num_float will be 10.5 (float)
print(num_float, type(num_float))  # Output: 10.5 <class 'float'>

# Converting an integer to a string
num_int = 10
num_str = str(num_int)  # num_str will be "10" (string)
print(num_str, type(num_str))  # Output: 10 <class 'str'>

# Converting a string to a boolean
bool_str = "True"
bool_val = bool(bool_str)  # bool_val will be True (boolean)
print(bool_val, type(bool_val))  # Output: True <class 'bool'>