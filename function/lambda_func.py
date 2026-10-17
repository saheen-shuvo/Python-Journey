# Lambda Function in Python
# Lambda functions are anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression. The expression is evaluated and returned.

# Example of a simple lambda function that adds two numbers:
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example of a lambda function that squares a number:
square = lambda x: x ** 2
# Working process: here, the lambda function takes one argument `x` and returns the square of `x`. When we call `square(4)`, it computes 4 squared, which is 16.
print(square(4))  # Output: 16

# Example of a lambda function used with the `map()` function to square a list of numbers:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example of a lambda function used with the `filter()` function to filter even numbers from a list:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Example of a lambda function used with the `sorted()` function to sort a list of tuples based on the second element:
tuples = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]

# Example of a lambda function used with the `reduce()` function from the `functools` module to compute the product of a list of numbers:
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120 (1*2*3*4*5 = 120)

# New column: Example of a lambda function used with the `max()` function to find the maximum value in a list:
max_value = max(numbers, key=lambda x: x)
print(max_value)  # Output: 5