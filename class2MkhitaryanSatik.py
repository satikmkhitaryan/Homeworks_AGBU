# def make_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#         print(f"We can  make triangle with this sides")
#     else:
#         print(f"We can not  make triangle with this sides")
#
#
# make_triangle(15, 20 ,7)
# make_triangle(15, 20 ,3)
#


class Car():
    def __init__(self, model, year, power):
        self.model = model
        self.year = year
        self.power = power

    def get_info_about_car(self):
        print(self.model, self.year, self.power)

    def __add__(self, other):
        model = self.model + other.model
        if self.year > other.year:
            year = self.year
        elif self.year < other.year:
            year = other.year
        else:
            year = None
        power = self.power + other.power
        return Car(model, year, power)

    def __gt__(self, other):
        if self.power > other.power:
            return True
        elif self.power < other.power:
            return False
    def __eq__(self, other):
        if self.power == other.power:
            return True

    def __len__(self):
        return len(self.model)

    def __int__(self):
        return self.year

    def __str__(self):
        return self.model

    def __bool__(self):
        return self


car1 = Car("Mersedes", 2010, 140)
car2 = Car("Opel", 2003, 135)
car3 = car2 + car1
car3.get_info_about_car()

if car1 > car2:
    print(f"Grather is {car1.model}")
elif car1 < car2:
    print(f"Grather is {car2.model}")
else:
    print("Cars are equal")


# print(len(car1))

# print(int(car1))

print(car1)
