name = input("Enter employee's name: ")
hoursWorked = eval(input("Enter number of hours worked in a week: "))
hourlyRate = eval(input("Enter hourly pay rate: "))
fedTaxRate = eval(input("Enter federal tax withholding rate: "))
stTaxRate = eval(input("Enter state tax withholding rate: "))

grossPay = hoursWorked*hourlyRate
fedWH = grossPay * fedTaxRate
stWH = grossPay * stTaxRate
totalDeduction = fedWH + stWH
netPay = grossPay - totalDeduction

print("\n\nEmployee Name:",name)
print("Hours Worked: ", hoursWorked)
print("Pay rate: ${0}".format(hourlyRate))
print("Gross Pay: ${0}".format(grossPay))
print("Deductions:")
print("\tFederal Withholding ({0}%): ${1}".format(fedTaxRate*100, fedWH))
print("\tState Withholding ({0}%): ${1}".format(stTaxRate*100, stWH))
print("\tTotal Deduction: ${0}".format(totalDeduction))
print("Net Pay: ${0}".format(netPay))
