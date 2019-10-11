principal = eval(input("Total initial loan amount: "))
years = eval(input("Years: "))

print("\n{0:17}{1:19}{2}\n".format('Interest Rate', 'Monthly Payment', 'Total Payment'))

for i in range(25):
    rateY = (5 + i*.125) / 100
    rateM = rateY / 12

    paymentM = principal * rateM / (1 - 1/ (1 + rateM) ** (years * 12))
    totalPayment = paymentM * years * 12

    print("{0:<17.3%}${1:<18.2f}${2:<0.2f}".format(rateY, paymentM, totalPayment))
