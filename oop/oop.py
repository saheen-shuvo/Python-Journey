# OOP in Python
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for the creation of reusable and modular code by encapsulating data and behavior into objects. Python is an object-oriented programming language that supports OOP concepts such as classes, objects, inheritance, polymorphism, and encapsulation.

# Class: A class is a blueprint for creating objects. It defines the attributes (data) and methods (functions) that the objects created from the class will have.
# Object: An object is an instance of a class. It has the attributes and methods defined by the class.

# Here's a simple example of OOP in Python:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age}.")

# Creating an object of the Person class
person1 = Person("Alice", 30)
person1.introduce()

# Inheritance: Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and establishes a relationship between classes.
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.student_id = student_id

    def introduce(self):
        super().introduce()  # Call the introduce method of the parent class
        print(f"My student ID is {self.student_id}.")

# Creating an object of the Student class
student1 = Student("Bob", 20, "S12345")
student1.introduce()

# Polymorphism: Polymorphism allows methods to have the same name but behave differently based on the object that calls them. This can be achieved through method overriding or operator overloading.
class Animal:
    def speak(self):
        pass  # This method will be overridden in child classes

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Creating objects of Dog and Cat classes
dog = Dog()
cat = Cat()
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!