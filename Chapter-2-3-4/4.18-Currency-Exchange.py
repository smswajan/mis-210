rate = eval(input("Enter the exchange rate from dollars to BDT: "))
method = eval(input("Enter 0 for dollar to BDT and 1 vice versa: " ))
if(method == 0):
    amount = eval(input("Enter dollar amount: "))
    bdt_amount = amount*rate
    print("${0} is {1} BDT".format(amount,bdt_amount))
elif(method == 1):
    amount = eval(input("Enter BDT amount: "))
    dollar_amount = amount/rate
    print("{0} BDT is ${1}".format(amount,dollar_amount))
else:
    print("Wrong method!")
