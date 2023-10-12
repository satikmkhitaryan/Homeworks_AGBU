# https://www.w3schools.com/python/python_lists.asp
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_sets.asp
# https://www.w3schools.com/python/python_dictionaries.asp

# 1. Write a Python program to get the largest number from a list.
myList = [5, 15, 58, 12, 45, 36, 97, 458, 15, 49]
myList.sort()
print(f"The largest number of list is {myList.pop()}")

# 2. Write a Python program to check a list is empty or not.
list1 = ["orange", "lemon", "banana"]
list2 = []
print("list1 is not empty" if len(list1) > 0 else "list1 is empty")
print("list2 is not empty" if len(list2) > 0 else "list2 is empty")

# or
if len(list1) > 0:
    print("list1 is not empty")
else:
    print("list1 is empty")



# 3. Write a Python program to remove all elements from a given set.
mySet = {5,10, "orange", "lemon"}
mySet.clear()
print(f"After removing elements we'll have {mySet}")



# 4. Write a Python program to check if a given value is present in a set or not.
mySet = {"apple", "banana", "cherry", "lemon", "watermelon"}
value1 = "watermelon"
value2 = "kiwi"
if value1 in mySet:
    print(f"{value1} is present in a set")
else:
    print(f"{value1} is not present in a set")

if value2 in mySet:
    print(f"{value2} is present in a set")
else:
    print(f"{value2} is not present in a set")


# 5. Write a Python program to convert a list to a tuple.
myList = ["orange", "apple", "banana", "kiwi"]
myTuple = tuple(myList)
print(f"Tuple converted from list is: {myTuple}")


# 6. Write a Python program to remove an item from a tuple.
tuple1 = ("apple", "banana", "cherry", "apple", "orange")
list1 = list(tuple1)
list1.remove("cherry")
print(f"After removing an item \"cherry\" tuple will be: {tuple(list1)}")


# 7. Write a Python script to check whether a given key already exists in a dictionary or not.


myDict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
key1 = "year"
if key1 in myDict:
    print(f"Key by name '{key1}' exists in  dictionary")
else:
    print(f"Key by name '{key1}' don't exist in  dictionary")

# or


if key1 in myDict.keys():
    print(f"Key by name '{key1}' exists in  dictionary")
else:
    print(f"Key by name '{key1}' don't exist in  dictionary")

# or


# 8. Write a Python script to merge two Python dictionaries.

dict1 = {
  "brand": "Ford",
  "model": "Mustang"
}
dict2 = {
    "year": 1964,
    "country": "China"
}
dict1.update(dict2)
print(f"After merging dictionaries we will have: {dict1}")

