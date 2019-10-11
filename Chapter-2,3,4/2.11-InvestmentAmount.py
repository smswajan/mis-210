finalAmount = eval(input("Enter final account value: "))
r = eval(input("Enter annual interest rate in percent: "))
y = eval(input("Enter number of years: "))

# Converting annual interest rate to monthly interest rate
r = r/1200

# Converting years to months
m = y * 12

initialDA = finalAmount/pow((1 + r), m)

print("Initial deposit value is: ", round(initialDA, 2))
