def calcIncTax(a, b, c, d, e, income):
    if income <=a:
        tax = income * .1
    elif income <= b:
        tax = a * .1 + (income - a) *.15
    elif income <= c:
        tax = a * .1 + (b-a)*.15 + (income-b)*.25
    elif income <= d:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (income - c)*.28
    elif income <= e:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (income -d)*.33
    else:
        tax = a * .1 + (b-a)*.15 + (c-b)*.25 + (d-c)*.28 + (e-d)*.33 + (income - e)*.35
    return tax

def computeTax(status, taxableIncome):
    if(status == "single"):
        a, b, c, d, e = 8350, 33950, 82250, 171550, 372950
        return calcIncTax(a, b, c, d, e, taxableIncome)
    elif status == "married-joint" :
        a, b, c, d, e = 16700, 67900, 137050, 208850, 372950
        return calcIncTax(a, b, c, d, e, taxableIncome)
    elif status == "married-separate" :
        a, b, c, d, e = 8350, 33950, 68525, 104425, 186475
        return calcIncTax(a, b, c, d, e, taxableIncome)
    elif status == "head" :
        a, b, c, d, e = 11950, 45500, 117450, 190200, 372950
        return calcIncTax(a, b, c, d, e, taxableIncome)
x = computeTax("single",50000)
print(x)
