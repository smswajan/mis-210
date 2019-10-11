salary = 5000
salesAmount = 0
while salary <= 30000:
    salesAmount += .01
    if salesAmount <= 5000:
        salary += .08 * .01
    elif salesAmount <= 10000:
        salary += .1 * .01
    else:
        salary += .12 * .01
salesAmount = round(salesAmount, 2)
print("To make $30000 salary the sales amount has to be:", salesAmount)
