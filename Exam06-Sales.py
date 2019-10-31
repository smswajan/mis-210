store_1 = eval(input("Enter today's total sales for store one (rounded to nearest $100): "))
store_2 = eval(input("Enter today's total sales for store two (rounded to nearest $100): "))
store_3 = eval(input("Enter today's total sales for store three (rounded to nearest $100): "))

for i in range(0,store_1, 100):
    print("*", end="")
print()
for j in range(0,store_2,100):
    print("*", end="")
print()
for k in range(0, store_3, 100):
    print("*", end="")
