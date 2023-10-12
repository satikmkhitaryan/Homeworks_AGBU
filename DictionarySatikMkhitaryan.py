

# #9.
myList = ["orange", "apple", "kiwi"]
print(f"myList is: {myList}")
inp1 = input("Please input a word: ")
inp2 = input("Please input another word: ")
myList.insert(0, inp1)
myList.append(inp2)
print(myList)

#10.

myTuple = ("banana", "pear", "apple", "banana")
a = myTuple.count(myTuple[0])
print(a)

# 11.

mySet = {"name", "lastName"}
thisList = list((mySet))
thisList[0] = thisList[0].capitalize()
mySet = set((thisList))
print(mySet)

# 12.

myDict = {"name" : "John",
          "lastName" : "Smith",
          "address" : "New-York"}

dict2 = {"car" : "BMW"}
myDict.update(dict2)
print(myDict)

