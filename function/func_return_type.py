# Function Return Types in Python

# No Return type
def greet():
    print("Hello, welcome to the world of Python!")

# calling the function
greet()

# Using Parameters and No Return Value
def greet_user(name):
    print(f"Hello, {name}! Welcome to the world of Python!")
    return f"Hello, {name}! Welcome to the world of Python!"
# calling the function
greet_user("Alice")

# Using default Parameters and No Return Value
def greet_user(name="User"):
    print(f"Hello, {name}! Welcome to the world of Python!")
    return f"Hello, {name}! Welcome to the world of Python!"
# calling the function
greet_user()

# Using Parameters and Return Value
def add_numbers(a, b):
    return a + b
# calling the function
result = add_numbers(5, 3)
print(f"The sum is: {result}")

# unzipping the return values
def get_user_info():
    name = "Alice"
    age = 30
    city = "New York"
    return name, age, city  

# calling the function and unzipping the return values
name, age, city = get_user_info()
print(f"Name: {name}, Age: {age}, City: {city}")

# train_test_split function from sklearn library returns multiple values, which can be unpacked into separate variables
from sklearn.model_selection import train_test_split # type: ignore

# Example usage of train_test_split
X = [[1, 2], [3, 4], [5, 6], [7, 8]]
y = [0, 1, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("Training data:")
print("X_train:", X_train)
print("y_train:", y_train)

print("Testing data:")
print("X_test:", X_test)
print("y_test:", y_test)