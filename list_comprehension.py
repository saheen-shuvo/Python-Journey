# List Comprehension

even = [];

# Naive
for i in range(100):
    if i % 2 == 0:
        even.append(i)

print("Even numbers from 0 to 99:", even)

# List Comprehension
random_list = [x for x in range(100) if x % 2 == 0]

print("Even numbers from 0 to 99 using list comprehension:", random_list)


# List Comprehension with strings

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
capitalized_fruits = []

for fruit in fruits:
    capitalized_fruits.append(fruit.upper())

print("Capitalized fruits:", capitalized_fruits)

# List Comprehension with strings
capitalized_fruits_comprehension = [fruit.upper() for fruit in fruits]

print("Capitalized fruits using list comprehension:", capitalized_fruits_comprehension)