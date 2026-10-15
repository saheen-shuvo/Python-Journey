# Arguments in Python are the values that are passed to a function when it is called. They can be of any data type, including numbers, strings, lists, dictionaries, and even other functions. Arguments allow functions to accept input and perform operations based on that input.

# Positional Arguments
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Example of calling the function with positional arguments
greet_user("Alice", 30)

# Keyword Arguments
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Example of calling the function with keyword arguments
greet_user(name="Bob", age=25)

# Default Arguments
def greet_user(name="User", age=18):
    print(f"Hello, {name}! You are {age} years old.")

# Example of calling the function with default arguments
greet_user()

# Variable-length Arguments
def greet_users(*names):
    for name in names:
        print(f"Hello, {name}! Welcome to the world of Python!")    

# Example of calling the function with variable-length arguments
greet_users("Alice", "Bob", "Charlie")

# Keyword Variable-length Arguments
def greet_users(**user_info):
    print("User Information:", user_info) #outputs the dictionary of user information
    for key, value in user_info.items():
        print(f"{key}: {value}")

# Example of calling the function with keyword variable-length arguments
greet_users(name="Alice", age=30, city="New York")