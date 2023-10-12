# 1*. Write a Python program that accepts a word from the user and reverse it.
"""
word = input("Please enter a word \n")
# reversed = word[::-1]
# print(reversed)
​
reversed = ""
for i in word:
    reversed[]
​
​
​
# 2. Write a Python program to count that user inputed number is even or odd.
number = int(input("Please enter a number \n"))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
​
​
# 3. Write a Python program to find is inputed number in 100 to 400 (both included). Hint(dont google task description)
number = int(input("Please enter a number \n"))
if number >= 100 and number <= 400:
    print(f"{number} is in range 100 to 400.")
else:
    print(f"{number} isn't in range 100 to 400.")
​
​
​
# 4. Write a Python program that get 2 numbers from user and return Biggest, Median, Sum, Multiply, Divide and Subtract
num1 = int(input("Please enter a number \n"))
num2 = int(input("Please enter another number \n"))
if num1 > num2:
    print(f"{num1} is the biggest")
elif num1 < num2:
    print(f"{num2} is the biggest")
else:
    print(f"{num1} and {num2} are equal")
​
print(f"The medium of {num1}  and {num2} is {(num1 + num2) / 2}")
print(f"{num1} plus {num2}  equals  {num1 + num2}")
print(f"{num1} times to {num2}  equals  {num1 * num2}")
print(f"{num1} divided by {num2}  equals  {num1 / num2}")
print(f"{num1} minus  {num2}  equals  {num1 - num2}")
​
​
# 5. Write a Python program to get next day of a given date.
#    Expected Output:
#    Input a year: 2016
#    Input a month [1-12]: 8
#    Input a day [1-31]: 23
#    The next date is [yyyy-mm-dd] 2016-8-24
#
#
​
​
year = int(input("Please enter a year\n"))
month = int(input("Please enter a month\n"))
day = int(input("Please enter a day\n"))
if day <= 31 and month != 2 and month < 12:
    if (month == 4 or month == 6 or month == 9 or month == 11):
        if day > 30:
            print("Please enter valid date")
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1
        next_day = print(f"The next date is: {year}-{month}-{day}")
    elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
        if day > 31:
            print("Please enter valid date")
        if day == 31:
            day = 1
            month += 1
        else:
            day += 1
        next_day = print(f"The next date is: {year}-{month}-{day}")
elif month == 2:
    if (year % 4 != 0 and day > 28) or (year % 4 == 0 and day > 29):
        print("Please enter valid date")
    elif (year % 4 != 0 and day == 28) or (year % 4 == 0 and day == 29):
         month += 1
         day = 1
         next_day = print(f"The next date is: {year}-{month}-{day}")
    else:
        day += 1
        next_day = print(f"The next date is: {year}-{month}-{day}")
if (month == 12 and day == 31):
     day = 1
     month = 1
     year += 1
     next_day = print(f"The next date is: {year}-{month}-{day}")
else:
    print("Please enter valid date")

"""