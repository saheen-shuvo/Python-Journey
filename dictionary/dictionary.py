# Dictionary in Python is a collection of key-value pairs. Each key is unique and is used to access the corresponding value. Dictionaries are mutable, meaning that they can be changed after their creation. They are defined using curly braces {} and consist of key-value pairs separated by colons.

# Unique keys in a dictionary: Each key in a dictionary must be unique. If you try to add a duplicate key, the existing value will be updated with the new value.

# Mutable nature of dictionaries: Dictionaries are mutable, which means you can add, remove, or change key-value pairs after the dictionary has been created. However, the keys themselves must be immutable (e.g., strings, numbers, tuples).

#Ordered nature of dictionaries: As of Python 3.7, dictionaries maintain the insertion order of key-value pairs. When you iterate over a dictionary, the order of elements will be the same as the order in which they were added.

# Key Value pairs in a dictionary: Each key in a dictionary is associated with a value. You can access the value by using the corresponding key. Example: `my_dict[key]` will return the value associated with `key`. 

# Declaration of a empty dictionary
my_dict = {}
print(type(my_dict))  # Output: <class 'dict'>

# Declaration of a dictionary with key-value pairs
my_dict = {
    "Name": "John",
    "Age": 30,
    "City": "New York"
}
print(my_dict)  # Output: {'Name': 'John', 'Age': 30, 'City': 'New York'}

# Accessing values in a dictionary: You can access the value associated with a specific key using square brackets `[]`. If the key does not exist, it will raise a KeyError.
print("Name:", my_dict["Name"])  # Output: John
print("Age:", my_dict["Age"])    # Output: 30
print("City:", my_dict["City"])  # Output: New York

# Using get() method to access values: The `get()` method allows you to access the value associated with a key without raising a KeyError if the key does not exist. Instead, it returns `None` or a specified default value.
print("Name:", my_dict.get("Name"))  # Output: John
print("Age:", my_dict.get("Age"))    # Output: 30
print("City:", my_dict.get("City"))  # Output: New York

# Assignment of values in a dictionary: You can assign a value to a key in a dictionary using the assignment operator `=`. If the key already exists, its value will be updated; if the key does not exist, a new key-value pair will be added.
my_dict["Age"] = 31  # Update existing key
my_dict["Country"] = "USA"  # Add new key-value pair
print(my_dict)  # Output: {'Name': 'John', 'Age': 31, 'City': 'New York', 'Country': 'USA'}

# Removing key-value pairs from a dictionary: You can remove a key-value pair from a dictionary using the `del` statement or the `pop()` method. The `del` statement removes the key-value pair associated with the specified key, while the `pop()` method removes the key-value pair and returns the value associated with the specified key.
del my_dict["City"]  # Remove key-value pair using del
print(my_dict)  # Output: {'Name': 'John', 'Age': 31, 'Country': 'USA'}

# Using pop() method to remove key-value pairs: The `pop()` method removes the key-value pair associated with the specified key and returns the value associated with that key. If the key does not exist, it raises a KeyError unless a default value is provided.
removed_value = my_dict.pop("Age", None)  # Remove key-value pair using pop
print("Removed value:", removed_value)  # Output: 31
print(my_dict)  # Output: {'Name': 'John', 'Country': 'USA'}