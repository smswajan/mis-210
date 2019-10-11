loanAmount = eval(input("Total amount of loan: "))
years = eval(input("Number of years: "))
rateY = eval(input("Annual interest rate (e.g. 8): "))

rateM = rateY/1200

paymentM = loanAmount * rateM / (1 - 1/ (1 + rateM) ** (years*12))



totalPayment = paymentM * years * 12

print('\nMonthly payment: ', round(paymentM, 2))
print('Total payment: ', round(totalPayment, 2))
print()

balance = loanAmount

print("\n{0:12}{1:12}{2:12}{3:12}\n".format("Payment#","Interest", "Principal", "Balance"))

for i in range (12*years):
    interest = rateM*balance
    principal = paymentM - interest
    balance = balance - principal

    print("{0:4}{1:14}{2:13}{3:12}".format(round(i+1,2), round(interest,2), round(principal,2), round(balance,2)))

