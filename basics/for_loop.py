# FOR LOOP IN PYTHON

for i in range(5):
    print(i, "Hello World!")

# Output:
#0  Hello World!
#1  Hello World!
#2  Hello World!
#3  Hello World!
#4  Hello World!

# So range function generates a sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified (5) number. In this case, it generates numbers from 0 to 4.


# Range Function can have 3 parameters: start, stop, step

# range(start, stop, step) 

for i in range(1, 10, 2):
    print(i, "Hello World!")

# Output:
#1  Hello World!
#3  Hello World!
#5  Hello World!
#7  Hello World!
#9  Hello World!