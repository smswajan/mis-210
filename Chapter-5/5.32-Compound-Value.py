savingsAmount = eval(input("Enter the monthly savings amount: "))
annualIntRate = eval(input("Enter the annual interest rate (e.g. 5): "))
months = eval(input("Enter the number of months to continue savings: "))

monthlyIntRate = annualIntRate/100/12

totalSavings = 0

for i in range(months):
    totalSavings = (savingsAmount + totalSavings)*(1+monthlyIntRate)
print("At {0}% annual interest rate, with the monthly savings of ${1} for {2} months, the amount in the savings account will be ${3}.".format(annualIntRate, savingsAmount, months,round(totalSavings, 2)))
