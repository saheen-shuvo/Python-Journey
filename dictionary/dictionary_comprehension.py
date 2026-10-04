# Dictionary Comprehension in Python
# Dictionary comprehension is a concise way to create dictionaries in Python. It allows you to generate key-value pairs in a single line of code using a specific syntax. The general syntax for dictionary comprehension is:
# {key_expression: value_expression for item in iterable if condition}  

squares = {x: x**2 for x in range(1, 6)}  # Create a dictionary of squares from 1 to 5
print("Squares:", squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

co_ordination = [(1, 2), (3, 4), (5, 6), (7, 8)]
location = ["dhaka", "chittagong", "khulna", "rajshahi"]


exact_location = {co_or: loc for co_or, loc in zip(co_ordination, location)}  # Create a dictionary from two lists using zip
print("Exact Location:", exact_location)  # Output: {(1, 2): 'dhaka', (3, 4): 'chittagong', (5, 6): 'khulna', (7, 8): 'rajshahi'}