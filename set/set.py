# Set in python: A set is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from a set after its creation. Sets are defined by enclosing the elements in curly braces `{}` or by using the built-in `set()` function.

# Unique elements in a set: Sets automatically eliminate duplicate elements. If you try to add a duplicate element to a set, it will be ignored.

# mutable nature of sets: Sets are mutable, which means you can add or remove elements from a set after its creation. However, the elements themselves must be immutable (e.g., numbers, strings, tuples).

# unordered nature of sets: Sets do not maintain the order of elements. When you iterate over a set, the order of elements may not be the same as the order in which they were added.

# Declaration of a set
my_set = {1, 2, 3, 4, 5}

print("Set:", my_set)

# Type of the set
print("Type of my_set:", type(my_set))  # Output: <class 'set'>

# Empty set declaration
empty_set = set()  # Use set() to create an empty set
print("Empty set:", empty_set)
print("Type of empty_set:", type(empty_set))  # Output: <class 'set'>

# Accessing elements in a set: You cannot access elements in a set using indexing or slicing, as sets are unordered. However, you can iterate over the elements of a set using a loop.
print("Iterating over my_set:")
for element in my_set:
    print(element)

# Check if an element exists in a set
if 3 in my_set:
    print("3 is in the set")
if 6 in my_set:
    print("6 is in the set")
else:
    print("6 is not in the set")

# Sum of elements in a set
print("Sum of elements in my_set:", sum(my_set))

print("Set after adding 6:", my_set)

# Adding elements to a set
my_set.add(6)  # Add a single element

# Adding multiple elements to a set
my_set.update([7, 8, 9])  # Add multiple elements using update

# Removing elements from a set
my_set.remove(2)  # Remove an element (raises KeyError if the element is not found)
my_set.discard(10)  # Remove an element (does not raise an error if the element is not found)

# Remove using pop() method (removes and returns an arbitrary element)
removed_element = my_set.pop()
print("Removed element:", removed_element)
print("Set after popping an element:", my_set)

# Clearing a set
my_set.clear()  # Remove all elements from the set

# Set operations: Sets support various mathematical operations like union, intersection, difference, and symmetric difference.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of sets
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

# Symmetric difference of sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)

# Subset
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# Superset
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# Disjoint
is_disjoint = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", is_disjoint)

# Set methods: Sets have several built-in methods that allow you to perform various operations on sets. Some commonly used set methods include:
# 1. add(): Adds an element to the set.
# 2. update(): Adds multiple elements to the set.
# 3. remove(): Removes an element from the set (raises KeyError if the element is not found).
# 4. discard(): Removes an element from the set (does not raise an error if the element is not found).  
# 5. pop(): Removes and returns an arbitrary element from the set.
# 6. clear(): Removes all elements from the set.
# 7. union(): Returns a new set that is the union of two sets.
# 8. intersection(): Returns a new set that is the intersection of two sets.
# 9. difference(): Returns a new set that is the difference of two sets.
# 10. symmetric_difference(): Returns a new set that is the symmetric difference of two sets.
# 11. issubset(): Returns True if all elements of the set are in the specified set.
# 12. issuperset(): Returns True if all elements of the specified set are in the set.
# 13. isdisjoint(): Returns True if the set has no elements in common with the specified set.