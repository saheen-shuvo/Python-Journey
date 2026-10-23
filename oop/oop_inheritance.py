# Inheritance in Python
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reusability and establishes a relationship between classes.

# Single Inheritance: In single inheritance, a child class inherits from a single parent class. The child class can access the attributes and methods of the parent class.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting.")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def open_trunk(self):
        print(f"The trunk of {self.brand} {self.model} is opening.")

# Creating an object of the Car class
car1 = Car("Toyota", "Camry", 4)
car1.start_engine()  # Output: The engine of Toyota Camry is starting.
car1.open_trunk()    # Output: The trunk of Toyota Camry is opening.

# Multiple Inheritance: In multiple inheritance, a child class can inherit from more than one parent class. This allows the child class to access attributes and methods from multiple parent classes.

class Electric:
    def charge(self):
        print("The vehicle is charging.")

class Hybrid(Vehicle, Electric):
    def __init__(self, brand, model, battery_capacity):
        Vehicle.__init__(self, brand, model)
        self.battery_capacity = battery_capacity

    def display_battery(self):
        print(f"The battery capacity of {self.brand} {self.model} is {self.battery_capacity} kWh.")

# Creating an object of the Hybrid class
hybrid_car = Hybrid("Toyota", "Prius", 8.8)
hybrid_car.start_engine()      # Output: The engine of Toyota Prius is starting.
hybrid_car.charge()            # Output: The vehicle is charging.
hybrid_car.display_battery()   # Output: The battery capacity of Toyota Prius is 8.8 kWh.

