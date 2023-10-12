
#
# class People():
#     def __init__(self, name):
#         self.__pass = "lll"
#         self.name = name
#
#     def login(self):
#         print(self.__pass)
#
# class Student(People):
#     def __init__(self, name, lName):
#         super.__init__(name)
#         self.lName = lName
#
# people1 = People("John")
# print(people1.name)
# people1.login()
# print(people1.__pass)
# class Animal():
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#         self.__age = None
#
#     def set_age(self, age):
#         self.__age = age
#         print("Type age")
#     def get_age(self):
#         print(f"Age is {self.__age}")
#
#     def eating(self):
#         print("Eating....")
#
#     def get_information_about_animal(self):
#         print(f"type is: {self.type}, name is: {self.name}")
#
# class Domestic(Animal):
#     def __init__(self, type, name, food):
#         super().__init__(type, name)
#         self.food = food
#
#     def eating(self):
#
#         print(f"{self.name} is eating {self.food}")
#         super().eating()
#
#
# class Wild(Animal):
#     def __init__(self, type, name, food):
#         self.food = food
#         super().__init__(type, name)
#
#     def eating(self):
#         super().eating()
#         print(f"{self.name} is eating {self.food}")
#
# animalWild = Wild("wild", "lion", "meat")
# animalDomestic = Domestic("domestic", "cow", "grass")
#
# animalWild.eating()
# animalWild.get_information_about_animal()
# print("----")
# animalDomestic.eating()
# animalDomestic.get_information_about_animal()
#
#
# animalDomestic.set_age(10)
# animalDomestic.get_age()




