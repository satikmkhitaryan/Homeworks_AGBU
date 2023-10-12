# https://www.w3schools.com/python/python_classes.asp
# https://www.w3schools.com/python/python_inheritance.asp
# https://www.geeksforgeeks.org/constructors-in-python/?ref=lbp
# https://www.geeksforgeeks.org/inheritance-in-python/?ref=lbp
# https://www.geeksforgeeks.org/encapsulation-in-python/?ref=lbp
# https://www.geeksforgeeks.org/polymorphism-in-python/?ref=lbp


# 1.  Write a class named Student with two attributes student_id, student_name. Add a new attribute student_class.
#     Create a function to display the entire attribute and their values in Student class.

class Student():
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def set_student_class(self, student_class):
        self.student_class = student_class

    def get_info_about_student(self):
        print(f"Student name is: {self.student_name}, ID is: {self.student_id}, class is: {self.student_class}")


student1 = Student("TS009", "John")
student1.set_student_class("2-nd")
student1.get_info_about_student()


# 2. Create a Vehicle class without any variables and methods
class Vehicle():
    def __init__(self):
        pass


# 3. Write a program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f"max.speed is: {self.max_speed} \nmileage is: {self.mileage}")


car1 = Vehicle(300, 1000)
car1.get_info()


# 4. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f"max.speed is: {self.max_speed}\n mileage is: {self.mileage}")

class Bus(Vehicle):
    def __init__(self,max_speed, mileage, model):
        super().__init__(max_speed, mileage)
        self.model = model

    def get_info(self):
        print(f"Our model is: {self.model}\n max.speed is: {self.max_speed} \nmileage is: {self.mileage}")

bus1 = Bus(300, 600, "MAN")
bus1.get_info()


# 5. Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f"max.speed is: {self.max_speed}\n mileage is: {self.mileage}")


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, model):
        super().__init__(max_speed, mileage)
        self.model = model
        self.capacity = 50

    def get_info(self):
        print(f"Our model is: {self.model}\n max.speed is: {self.max_speed} \nmileage is: {self.mileage}\n seating capacity is: {self.capacity}")




bus1 = Bus(300, 600, "MAN")
bus1.get_info()
