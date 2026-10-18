# Exception in Python is a mechanism that allows you to handle errors gracefully during the execution of a program. When an error occurs, Python raises an exception, which can be caught and handled using try-except blocks. This prevents the program from crashing and allows you to provide meaningful error messages or take corrective actions.

# Here's a simple example of exception handling in Python:

# Example 1: Handling a ZeroDivisionError
try:
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 2: Handling a FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The specified file was not found.")

# Example 3: Handling multiple exceptions
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 4: Using the else and finally blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", result)
finally:
    print("Execution completed. This block will always run, regardless of whether an exception occurred or not.")

# In summary, exception handling in Python allows you to catch and handle errors gracefully, preventing program crashes and providing a better user experience. By using try-except blocks, you can manage different types of exceptions and take appropriate actions based on the specific error encountered.