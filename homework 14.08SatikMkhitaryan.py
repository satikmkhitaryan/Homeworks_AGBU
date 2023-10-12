 # 1. Write a program to display all three-digit numbers.

# for i in range(100, 1000):
#     print(i)

#     # or-------
# num = 100
# while num <= 999:
#     print(num)
#     num += 1

 # 2. Write a program to display all odd three-digit numbers.

# for i in range(100, 1000):
#     if i % 2 != 0:
#         print(i)

# # or
#
# num = 101
# while num <=999:
#     print(num)
#     num += 2
#
#
#
# # 3. Write a program to display even five-digit numbers in one line.
#
# num = 10000
# while num < 100000:
#     if num % 2 == 0:
#         print(num, end = "")
#         num += 2
#
# # or
# for i in range(10000, 99999, 2):
#     print(i, end = "")
#
#
# # 4. Write a program to display all numbers till 1000, which are divided both by 5 and 7.
#
# for i in range(1, 1000):
#     if i % 5 == 0 and i % 7 ==0:
#         print(i)

# # 5. Write a program to display every third element of the list.
#
# myList = [5, 4, 8, 65, 14, 89, 2, 45, 68, 74, 95, 28, 31, 64, 97, 82, 71, 93, 41, 63, 55]
#
# for i in range(len(myList) - 1):
#     if i % 3 == 0:
#         print(myList[i])
#
#  # 6. Write a program to display only lowercase elements from the list. Note: list contains at least 15 - 20
myList = ["hello", "World", "yEREVANan", "Yerevan", "adDress", "name", "John", "Smith", "age", "Armenia", "town", "country"]
# newList = []
# for i in myList:
#     if i.islower():
#         newList.append(i)
# print(newList)



# --or
resultList = []
for item in myList:
    if item[0].islower():
        resultList.append(item)
i = 0
lengthOfList = len(myList)
while i < lengthOfList:
    if myList[i][0].islower():
        resultList.append(myList[i])
    i += 1

print(resultList)
print(len(resultList))

# --------------------------------


