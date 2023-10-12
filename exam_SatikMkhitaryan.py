# Exercise 1: Write a Python function called calculate_average that takes a list of
# numbers as input and returns the average (mean) of those numbers. Test your function
# with the following list: [10, 20, 30, 40, 50].
def calculate_average(myList):
    res = 0
    lenOfList = len(myList)
    for item in myList:
        res += item
    return f"The average  of list's numbers is equal to {res / lenOfList}"


list1 = [10, 20, 30, 40, 50]
print(calculate_average(list1))


# Exercise 2: Create a Python class called Rectangle with two attributes: width and
# height. Implement a method named calculate_area that calculates and returns the area
# of the rectangle. Then, create an instance of the Rectangle class with a width of 5 units
# and a height of 10 units. Calculate and print the area of the rectangle.

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        areaOfRectangle = self.width * self.height
        return f"The area  of this rectangle is equal to {areaOfRectangle}"


rectangle1 = Rectangle(5, 10)
print(rectangle1.calculate_area())
