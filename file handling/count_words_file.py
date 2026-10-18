# Count number of words in a file
from functools import reduce

with open("example.txt", "r") as file:
    strings_list = file.readlines()
    # find total number of lines
    words = strings_list.split()
    # find total number of words
    word_count = len(words)
    # find out words
    num_of_words = list(map(lambda x: len(x.split()), strings_list))
    # total number of words
    total_num_of_words = reduce(lambda x, y : x + y, num_of_words)
    # cleaning spaces and new line
    strings_list = list(map(str.strip, strings_list))
    strings_list = list(map(lambda x : x.replace(" ", ""), strings_list))

    num_of_characters = list(map(lambda x : len(x), strings_list))

    print("Number of char", num_of_characters)

    total_num_of_char = reduce(lambda x, y : x+y, num_of_characters)

    print("Total number of characters:", total_num_of_char)


    # w+, r+. a+ mode
    with open("example.txt", "r+") as file:
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
