num1 = int(input("Give the first integer: "))
num2 = int(input("Give the second integer: "))

if num1 < num2:
    divisor = num1
while divisor >= 1:
    if num1%divisor == 0 and num2%divisor == 0:
        break
    divisor = divisor - 1
print("The greatest common divisor is", divisor)
