depositAmount = eval(input("Enter the initial deposit amount: "))
yieldAnnual = eval(input("Enter annual percentage yield: "))
maturityPeriod = eval(input("Enter maturity period (number of months): "))

print("\n{0:12}{1:18}".format("Month", "CD Value"))

month = 1
while month <= maturityPeriod:
    depositAmount = depositAmount + depositAmount * yieldAnnual / 1200
    print("{0:3}{1:18}".format(month, round(depositAmount,2)))
    month = month + 1
