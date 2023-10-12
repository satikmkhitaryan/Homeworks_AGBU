
# 1. Write a Python program that print list elements count.
myList = ["a", "b", "c", "d","e"]
print(len(myList))

# # 2. Write a Python list use add, remove, elements use insert, append, pop, remove and extend methods.
myList =  ["apple", "banana", "cherry", "kiwi", "mango"]
# myList.insert(2, "lemon")
# print(myList)

myList.append("peach")
print(myList)

myList.remove("kiwi")
print(myList)

myList.pop(3)
print(myList)

otherList = [1,2,3]
myList.extend(otherList)
print(myList)

# 3. Write a Python program to check if a list is empty or not
thisList = ["apple", "banana", "cherry", "kiwi", "mango"]
if len(thisList) > 0:
    print(f"This list is not empty, because there is/are {len(thisList)} item/items")
else:
    print(f"This list is empty, because there is {len(thisList)} item")

#  or
print("This list is not empty" if len(thisList) > 0 else "This list is  empty" )

# 4. Write a Python program to create a tuple with different data types.
item1 = "banana"
item2 = 54
item3 = True
item4 = 15.5
item5 = ["kiwi", "orange"]
myTuple = tuple((item1, item2, item3, item4, item5))
print(myTuple)
print(f"Type is : {type(myTuple)}")

# 5. Write a Python program to create a tuple of numbers and print one item.
myTyple = (1, 2, 3, 5, 7)
print(myTyple[2])

# 6. Write a Python program to get the 4th element from the last element of a tuple.

thisTuple = ('apple', 'banana', 'cherry', 'kiwi', 'orange')
print(thisTuple[-4])

# Vardan
# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_tuples.asp
#
# 1. Write a Python program that print list elements count.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Count of list is: {len(myList)}")

# 2. Write a Python list use add, remove, elements use insert, append, pop, remove and extend methods.
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original List: {myList}")

myList.insert(0, 0)
print(f"Result after insertion: {myList}")

myList.append(10)
print(f"Result after append: {myList}")

myList.pop(9)
print(f"Result after pop: {myList}")

myList.remove(5)
print(f"Result after remove: {myList}")

myList2 = [11, 12, 13]
myList.extend(myList2)
print(f"Result after extend: {myList}")

# 3. Write a Python program to check if a list is empty or not
myList = [1, 2, 3, 4, 5, 6]

if len(myList) == 0:
    print("List Is empty")
else:
    print("List is not empty")

# 4. Write a Python program to create a tuple with different data types.
myTuple = (1, 3.14, "Hello", True)
print(f"Tuple with different data types is: {myTuple}")

# 5. Write a Python program to create a tuple of numbers and print one item.
myTuple = (1, 3.14, "Hello", True)
print(f"Second element from tuple is: {myTuple[1]}")

# 6. Write a Python program to get the 4th element from the last element of a tuple.
myTuple = (1, 3.14, "Hello", True)
print(f"4th element from end is: {myTuple[-4]}")
print(myList[-1,-3])