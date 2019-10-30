weight = eval(input("Enter your weight in pounds: "))

feet = eval(input("Enter Feet: "))
inch = eval(input("Enter inch: "))
height = inch + feet*12

kiloPerPound = 0.45359
meterPerInch = 0.0254

weightInKilo = weight * kiloPerPound
heightInMeters = height * meterPerInch
bmi = weightInKilo / pow(heightInMeters, 2)
bmi = round(bmi,2)
print("BMI is", bmi)

if bmi < 18.5:
    print("You are UNDERWEIGHT")
elif bmi < 25:
    print("You are NORMAL")
elif bmi < 30:
    print("You are OVERWEIGHT")
else:
    print("You are OBESE")
