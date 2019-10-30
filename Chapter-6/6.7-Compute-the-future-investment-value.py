def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    months = years * 12
    futureInvestmentValue = investmentAmount * pow((1+monthlyInterestRate), months)
    return futureInvestmentValue

investmentAmount = eval(input("The amount invested: "))
annualInterestRate = eval(input("Annual interest rate: "))

monthlyInterestRate = annualInterestRate / 1200

print("Years    Future Value")
for i in range(1, 31):
    print("{0:4} {1:12}".format(i, round(futureInvestmentValue(investmentAmount, monthlyInterestRate, i), 2)))
