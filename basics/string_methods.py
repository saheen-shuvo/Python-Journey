# String Methods in Python are built-in functions that allow you to manipulate and work with strings. Here are some commonly used string methods:

# 1. `len()`: Returns the length of the string.
my_string = "Hello, World!"
length = len(my_string)  # 13
print(length)  # 13

# 2. string in: Checks if a substring exists within the string.
substring_exists = "World" in my_string  # True
print(substring_exists)  # True

# 3. string.upper(): Converts all characters in the string to uppercase.
upper_string = my_string.upper()  # 'HELLO, WORLD!'
print(upper_string)  # 'HELLO, WORLD!'

# 4. string.lower(): Converts all characters in the string to lowercase.
lower_string = my_string.lower()  # 'hello, world!'
print(lower_string)  # 'hello, world!'

# 5. string.strip(): Removes leading and trailing whitespace from the string.
string_with_whitespace = "   Hello, World!   "
stripped_string = string_with_whitespace.strip()  # 'Hello, World!'
print(stripped_string)  # 'Hello, World!'

# 6. find(): Returns the index of the first occurrence of a substring in the string. Returns -1 if the substring is not found.
index_of_substring = my_string.find("World")  # 7
print(index_of_substring)  # 7

# 7. rfind(): Returns the index of the last occurrence of a substring in the string. Returns -1 if the substring is not found.
last_index_of_substring = my_string.rfind("o")  # 8
print(last_index_of_substring)  # 8

# 8. count(): Returns the number of occurrences of a substring in the string.
count_of_substring = my_string.count("o")  # 2
print(count_of_substring)  # 2

# 9. replace(): Replaces occurrences of a substring with another substring.
replaced_string = my_string.replace("World", "Python")  # 'Hello, Python!'
print(replaced_string)  # 'Hello, Python!'

# 10. split(): Splits the string into a list of substrings based on a specified delimiter (default is whitespace).
split_string = my_string.split(", ")  # ['Hello', 'World!']
print(split_string)  # ['Hello', 'World!']

# 11. join(): Joins a list of strings into a single string with a specified delimiter.
list_of_strings = ["Hello", "World!"]   
joined_string = ", ".join(list_of_strings)  # 'Hello, World!'
print(joined_string)  # 'Hello, World!'

# 12. endswith(): Checks if the string ends with a specified substring.
ends_with_exclamation = my_string.endswith("!")  # True
print(ends_with_exclamation)  # True

# 13. startswith(): Checks if the string starts with a specified substring.
starts_with_hello = my_string.startswith("Hello")  # True
print(starts_with_hello)  # True