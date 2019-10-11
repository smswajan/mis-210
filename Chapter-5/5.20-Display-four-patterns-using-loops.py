#Pattern A
print("Pattern A")
for i in range(1, 7):
    for j in range(1, i+1):
        print(format(j, "2d"), end="")
    print("")

#Pattern B
print("\n\nPattern B")
for i in range(1, 7):
    for j in range(1, 8-i):
        print(format(j, "2d"), end="")
    print()

#Pattern C
print("\n\nPattern C")
for i in range(1, 7):
    for j in range(6, 0, -1):
        if j <= i:
            print(format(j, "2d"), end="")
        else:
            print(" ", end= " ")
    print()

#Pattern D
print("\n\nPattern D")
for i in range(1, 7):
    for j in range(1, 8-i):
        print(format(j, "2d"), end="")
    print()


'''----------------------------
------ It's not necessary-----
--------- Skip This ----------

print("\n\nPattern D")
for i in range(1, 7):
    for j in range(6, 0, -1):
        if j <= 7-i:
            print(format(j, "2d"), end="")
        else:
            print(" ", end= " ")
    print()
--------------------------------'''
