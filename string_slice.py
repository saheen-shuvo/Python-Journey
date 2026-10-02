# String in Python is a sequence of characters. Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

# example of string slicing in Python
my_string = "Hello, World!"

# Accessing characters using indexing
first_character = my_string[0]  # 'H'
last_character = my_string[-1]  # '!'

# Multiline string
example_multiline_string = """This is a
multiline string in Python."""

# Slice the string to get a substring
# string slicing syntax: string[start:end] where start is the starting index (inclusive) and end is the ending index (exclusive)
# string[start: end: step] where step is the step size (optional)
substring = my_string[7:12]  # 'World'