# Polymorphism in Python refers to the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name.

# Method Overriding: In method overriding, a child class provides a specific implementation of a method that is already defined in its parent class. This allows the child class to modify or extend the behavior of the parent class method.
class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("Dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("Cat meows.")

# Creating objects of the Dog and Cat classes
dog = Dog()
cat = Cat()
dog.make_sound()  # Output: Dog barks.
cat.make_sound()  # Output: Cat meows.

# Method Overloading: In Python, method overloading is not natively supported as it is in some other programming languages. However, we can achieve similar behavior by using default arguments or variable-length arguments in methods.
class Calculator:
    def add(self, a, b=0):
        return a + b

# Creating an object of the Calculator class
calc = Calculator()
# Calling the add method with different numbers of arguments
result1 = calc.add(5)        # Output: 5 (5 + 0)
result2 = calc.add(5, 10)    # Output: 15 (5 + 10)
print(result1)  # Output: 5
print(result2)  # Output: 15

