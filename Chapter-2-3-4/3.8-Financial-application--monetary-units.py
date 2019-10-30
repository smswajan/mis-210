import decimal
amount = eval(input("Enter an amount in cents, for example, for 32.45 write 3245 "))

damount = str(amount)
damount = decimal.Decimal(damount)
dpoint = abs(damount.as_tuple().exponent)

damount = int(amount * pow(10, dpoint))

dollars = int(amount)

remainingAmount = damount - dollars*pow(10, 2)

cents = remainingAmount

numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

print("Your amount", amount, "consists of\n",
     "\t", dollars, "dollars\n",
     "\t", numberOfQuarters, "quarters\n",
     "\t", numberOfDimes, "dimes\n",
     "\t", numberOfNickels, "nickels\n",
     "\t", numberOfPennies, "pennies\n")
