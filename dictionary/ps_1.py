# Q: Given a list of numbers, make a list with unique values.

lst = [1, 2, 3, 2, 4, 5, 1, 6, 3]

unique_values = set(lst)  # Convert the list to a set to get unique values

print("Unique values:", unique_values)  # Output: {1, 2, 3, 4, 5, 6}

# Convert the set back to a list 

lst = list(unique_values)
print("List with unique values:", lst)  # Output: [1, 2, 3, 4, 5, 6]