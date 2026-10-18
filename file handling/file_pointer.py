# File Pointer in Python

# Open a file in read mode
with open("example.txt", "r") as file:
    # Read the content of the file
    content = file.read()
    print("File Content:")
    print(content)

    # Get the current position of the file pointer
    position = file.tell() 
    print("Current Position of File Pointer:", position)

    # Move the file pointer to the beginning of the file
    file.seek(0)
    print("Position after seeking to the beginning:", file.tell())

    # Read the content of the file from the beginning
    content_from_beginning = file.read()
    print("File Content from Beginning:")
    print(content_from_beginning)