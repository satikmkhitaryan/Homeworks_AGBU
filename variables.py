# 1. Write a program to solve (x + y) * (x + y).
#       Test Data : x = 4, y = 3
#       Expected Output : (4 + 3) ^ 2) = 49
"""
x = 4
y = 3
result = (x + y) ** 2
print(f"({x} + {y}) ^ 2 = {result}")

# 2. Write a program to parse a string to Float or Integer
string = "10"
myInt = int(string)
myFloat = float(string)
print(f"Value is: {myInt} and type is: {type(myInt)}")
print(f"Value is: {myFloat} and type is: {type(myFloat)}")

# 3. Given variables x=30 and y=20, write a Python program to print "30+20=50" via variables

x = 30
y = 20
result = x + y
print(f"{x}+{y}={result}")


# 4. Write a program to get the Type, and Value of an variable

data = "python"
print(f"Variable's value is: {data} \n Variable's type is:  {type(data)}")

# 5. Write a program to get the volume of a sphere with radius 6
radius = 6
pi = 3.14
volumeSphere = 4/3 * pi * radius**3
print(f"The volume of a sphere with radius {radius} equal to {volumeSphere}")

# # 6. Write a program to display your details like name, age, address in three different lines
name = "Sam"
age = 40
address = "Yerevan"
print(f"My name is {name} \n I am {age} \n My address is {address} ")

# 7. Write a program to count the 7% of 500
percent = 7
num = 500
result = num / 100 * percent
print(f" {percent} % of {num} equal to {result}")

#     or with format
print("{} % of {} equal to {}".format(percent, num, result))

"""
