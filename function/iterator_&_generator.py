# Iterator with next() and iter()

# Create an iterator from a list
my_list = [1, 2, 3, 4, 5]
# Get an iterator using iter()
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4
print(next(my_iterator))  # Output: 5

# Generator Function
def my_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = my_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

lst = [ x for x in range(500)]

def data_loader(chunk_size, lst):
    for i in range(0,len(lst),chunk_size):
        yield lst[i:i+chunk_size]

x = data_loader(100, lst)
print(type(x)) # Output: <class 'generator'>

print(next(x)) # Output: [0, 1, 2, ..., 99]
print(next(x)) # Output: [100, 101, 102, ..., 199]