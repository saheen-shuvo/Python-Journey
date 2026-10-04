# Methods in Dictionary in Python

# Give a value when a value is not present in the dictionary: The `setdefault()` method returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value and returns that value. This is useful for initializing keys with default values.
my_dict = {"Name": "John", "Age": 30}
# Using setdefault() method to get a value or set a default value
value = my_dict.setdefault("City", "New York")  # If "City" is not present, it will be added with the value "New York"
print("Value of 'City':", value)  # Output: New York
print(my_dict)  # Output: {'Name': 'John', 'Age': 30, 'City': 'New York'}
print(dict.get("hi")) # Output: None
print(dict.get("hi", "Not found")) # Output: Not found

# Adding a value to a dictionary: You can add a new key-value pair to a dictionary by assigning a value to a new key. If the key already exists, its value will be updated.
my_dict["Country"] = "USA"  # Add new key-value pair
print(my_dict)  # Output: {'Name': 'John', 'Age': 30, 'City': 'New York', 'Country': 'USA'} 

# Deleting a key-value pair from a dictionary: You can delete a key-value pair from a dictionary using the `del` statement or the `pop()` method. The `del` statement removes the key-value pair associated with the specified key, while the `pop()` method removes the key-value pair and returns the value associated with the specified key.
del my_dict["Country"]  # Remove key-value pair using del

# Copying a dictionary: You can create a shallow copy of a dictionary using the `copy()` method. This creates a new dictionary with the same key-value pairs as the original dictionary.
my_dict_copy = my_dict.copy()  # Create a shallow copy of the dictionary    
print(my_dict_copy)  # Output: {'Name': 'John', 'Age': 31, 'City': 'Los Angeles'}

# Clearing a dictionary: You can remove all key-value pairs from a dictionary using the `clear()` method. This will leave you with an empty dictionary.
my_dict.clear()  # Remove all key-value pairs from the dictionary
print(my_dict)  # Output: {}

# Updating a dictionary: You can update a dictionary with key-value pairs from another dictionary using the `update()` method. If a key already exists in the original dictionary, its value will be updated; if the key does not exist, a new key-value pair will be added.
my_dict1 = {"Name": "Alice", "Age": 25}
my_dict2 = {"Age": 30, "City": "Los Angeles"}
my_dict1.update(my_dict2)  # Update my_dict1 with key-value pairs from my_dict2
print(my_dict1)  # Output: {'Name': 'Alice', 'Age': 30, 'City': 'Los Angeles'}

# Getting all keys from a dictionary: You can get a view of all the keys in a dictionary using the `keys()` method. This returns a view object that displays a list of all the keys in the dictionary.
my_dict = {"Name": "John", "Age": 30, "City": "New York"}
keys = my_dict.keys()  # Get all keys from the dictionary
print("Keys:", keys)  # Output: dict_keys(['Name', 'Age', 'City'])

# Getting all values from a dictionary: You can get a view of all the values in a dictionary using the `values()` method. This returns a view object that displays a list of all the values in the dictionary.
values = my_dict.values()  # Get all values from the dictionary
print("Values:", values)  # Output: dict_values(['John', 30, 'New York'])

# Getting all key-value pairs from a dictionary: You can get a view of all the key-value pairs in a dictionary using the `items()` method. This returns a view object that displays a list of all the key-value pairs in the dictionary.
items = my_dict.items()  # Get all key-value pairs from the dictionary
print("Items:", items)  # Output: dict_items([('Name', 'John'), ('Age', 30), ('City', 'New York')])

# Iterating over a dictionary: You can iterate over the keys, values, or key-value pairs in a dictionary using a for loop. This allows you to access each element in the dictionary one by one.
# Iterating over keys
for key in my_dict:
    print(key)
# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value) 