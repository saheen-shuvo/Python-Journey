# Write File in Python

# Open a file in write mode (creating a new file or overwriting an existing one)
with open("example.txt", "w") as file:
    # Write content to the file
    file.write("Hello, World!")

# Writing on an existing file (appending content)
with open("example.txt", "a") as file:
    # Append content to the file
    file.write("\nThis is an appended line.")

