def computeCommission(salesAmount):
    if salesAmount <= 5000:
        commission = salesAmount * .08
    elif salesAmount <= 10000:
        commission = 5000 * 0.08 + (salesAmount-5000) * .1
    else:
        commission = 5000 * 0.08 + 5000*.10 + (salesAmount-10000)*.12
    return commission
print("Sales Amount      Commission")

for i in range(10000, 100001, 5000):
    print("{0:4} {1:18}".format(i, computeCommission(i)))
