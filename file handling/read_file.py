# File Handling in Python
# File handling is an important aspect of programming that allows you to read from and write to files. Python provides built-in functions and methods to work with files, making it easy to perform various file operations. In this guide, we will cover the basics of file handling in Python, including opening files, reading from files, writing to files, and closing files.

# Opening Files:
# To open a file in Python, you can use the built-in `open()` function.
# The `open()` function takes two arguments: the file name and the mode in which you want to open the file. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'b' for binary mode.
# Example:
file = open('example.txt', 'r')  # Open a file in read mode 
print(file.read())  # Read the contents of the file
file.close()  # Close the file
print(file.closed)  # Output: True

# Reading from Files:
# You can read the contents of a file using various methods such as `read()`, `readline()`, and `readlines()`.
# Example:
file = open('example.txt', 'r')
print(file.read())  # Read the entire file
file.seek(0)  # Move the cursor to the beginning of the file
print(file.readline())  # Read the first line of the file
print(file.readlines())  # Read all lines of the file into a list
file.close()  # Close the file

# using for loop to read the file line by line
file = open('example.txt', 'r')
for line in file:
    print(line.strip())  # Print each line without extra newline characters
file.close()  # Close the file
