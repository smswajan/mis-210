tuitionFee = 10000
year = 0
total = 0

while year < 10:
    tuitionFee = tuitionFee * 1.05
    year = year + 1
tuitionFee = round(tuitionFee, 2)
print("Tuition at the end of 10 years is ${0}".format(tuitionFee))

while year < 14:
    tuitionFee = tuitionFee * 1.05
    year = year + 1
    total = total + tuitionFee
    
total = round(total, 2)
print("After 10 years, total cost of four years' tuition will be ${0}".format(total))
