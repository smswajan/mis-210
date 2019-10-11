investmentAmount = eval(input("Enter investment account: "))
r = eval(input("Enter annual interest rate : "))
y = eval(input("Enter number of years: "))

# Converting annual interest rate to monthly interest rate
monthlyIntRate = r/1200

# Converting years to months
m = y * 12

futureInvestment = investmentAmount*pow((1 + monthlyIntRate), m)

print("Initial deposit value is: ", round(futureInvestment, 2))
