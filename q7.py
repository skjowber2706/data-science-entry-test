class Car:
    """
    Task 1
    - create a class Car
    - has make, model, year
    - method to print car info
    """

    def __init__(self, make, model, year):
        # initilizing the atttributes
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        # printing the car detials
        print(str(self.year) + " " + self.make + " " + self.model)


# Task 2: creating object and runing method

# creating instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# calling the method
my_car.describe_car()
