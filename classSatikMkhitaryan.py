import math
class Animal():
    def __init__(self, type, name, age, feet):
        self.type = type
        self.name = name
        self.age = age
        self.feet = feet
    def eating(self):
        print(f"{self.name} is eating.")

    def make_sound(self, sound):
        print(f"{self.name} makes a sound {sound}")

    def get_information_about_animal(self):
        print(f"type is: {self.type}, name is: {self.name}, age is: {self.age}, feet count is: {self.feet}")

animal1 = Animal("mammal", "dog", 5, 4)
animal1.eating()
animal1.make_sound("gaf")
animal1.get_information_about_animal()

animal1 = Animal("bird", "hen", 1, 2)
animal1.eating()
animal1.make_sound("henSound")
animal1.get_information_about_animal()


class Student():
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    def learn(self):
        print(f"{self.name} is learning")

    def speaking(self, language):
        print(f"{self.name} is speaking in {language}")
    def get_info(self):
        print(f"Student name is {self.name}\n ID is: {self.ID}")

student1 = Student("John", 25)
student1.learn()
student1.speaking("english")
student1.get_info()

print("---------------------")
class Triangle():
    perimeter = 0
    surface = 0
    def __init__(self, side1, side2, side3, angle1):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1


    def perimeter_triangle(self):
        perimeter = self.side1 + self.side2 + self.side3
        print(f"Perimeter of triangle is equal to {perimeter}")
    def surface_triangle(self):
        if self.angle1 == 90:
            surface = self.side1 * self.side2 * 1/2
        else:
            surface = self.side1 * self.side2 * math.sin(self.angle1) * 1/2
        print(f"Surface of triangle is: {surface}")

triangle1 = Triangle(15, 20, 45, 30)
triangle1.perimeter_triangle()
triangle1.surface_triangle()
print(triangle1.side1 + triangle1.side2 + triangle1.side3)
print("-------------------")
def round_number(num):

    if int(num) == num:
        roundNum = int(num)
    else:
        roundNum = int(num) + 1
    return f"Round of number by ceil equal to {roundNum}"

print(round_number(5.1))
print("----------------")
def find_words_with_G(list):
    resultList = []
    for word in list:
        for letter in word:
            if letter == "g" or letter == "G":
                resultList.append(word)
                break
    return resultList

myList = ["Hello", "Gevorg", "fruits", "vegitables", "flower", "tiger", "lion"]
print(find_words_with_G(myList))

