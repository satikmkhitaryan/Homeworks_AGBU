rows = 5
for i in range(1, rows + 1):

    for j in range(i):
        print(i, end = " ")
    print(end= "\n")


rows = 5
for i in range(1, rows+1):
    for j in range(1, i + 1):
        print(j, end = " ")
        j += 1
    print("")

print("-----------")

rows = 5
b = 1
for i in range(1, rows + 1):
     for j in range(rows, 0, -1):
         print(b, end= " ")
         j -= 1
     b += 1
     print("")
