balance = eval(input("Enter the monthly saving amount:"))
r = 0.05/12
amount = 0
for i in range(6):
    amount = (balance+amount) * (1 + r)

print(round(amount, 2))
