# Define a class called Car with attributes make, model, and year.
# Create an instance of the Car class and print the attributes.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def description(self):
        return f"This car is of type {self.make} and the model is {self.model} and funnily enough this was first launched in {self.year}"
    def age(self):
        return 2024 - int(self.year)
car1 = Car("Tesla" + "Cybertruck" + "2024")
print(car1.make + car1.model + car1.year)

# Add a method called description that returns a string describing the car.
# Add another method called age that calculates how old the car is based on the current year.
# Call these methods and print the results.
print(car1.description())
print(car1.age())

# Define a class called ElectricCar that inherits from Car.
# Add an attribute battery_size and a method describe_battery that prints information about the battery.
# Create an instance of ElectricCar and call the methods from both the Car and ElectricCar classes.
class ElectricCar(Car):
    battery_size = 10
    def describe_battery(self):
        print(f"This battery has a size of {self.battery_size}")
electric_car1 = ElectricCar("Ford", "E-drive", "2021")
print(electric_car1.age())
print(electric_car1.describe())
print(electric_car1.describe_battery())