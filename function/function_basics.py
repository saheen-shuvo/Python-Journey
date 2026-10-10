#Function in Python is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# set of instructions that perform a specific task

# Defining a function


# def function_name(parameters):
    # code block
    # return result

# No Parameters and No Return Value
def greet():
    print("Hello, welcome to the world of Python!")

# calling the function
greet()

# Using Parameters and No Return Value
def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python!")

# calling the function
greet_user("Alice")

# Using default Parameters and No Return Value
def greet_user(name="User"):
    print(f"Hello, {name}! Welcome to the world of Python!")

# calling the function
greet_user()

# Using Parameters and Return Value
def add_numbers(a, b):
    return a + b

# calling the function
result = add_numbers(5, 3)
print(f"The sum is: {result}")

# Doc in functions
def greet_user(name):
    """This function greets the user with their name."""
    print(f"Hello, {name}! Welcome to the world of Python!")