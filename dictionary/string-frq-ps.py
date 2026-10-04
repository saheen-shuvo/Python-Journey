# Q: Given a string, count the frequency of each character and store it in a dictionary.

given_string = """data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data. Data science is related to data mining, machine learning and big data."""

words = given_string.split()  # Split the string into words

print("Words:", words)  # Output: List of words in the string

# Create an empty dictionary to store the frequency of each character
count_dict = {}

for word in words:
    count_dict[word] = count_dict.get(word, 0) + 1  # Increment the count for each word in the dictionary

print("Frequency of each word:", count_dict)  # Output: Dictionary with word frequencies