higherOrder = 1000
lowerOrder = 2

count = 0
numPerLine = 8

print("The prime numbers between 2 and 1000 are: \n")

while lowerOrder <= higherOrder:
    isPrime = True

    divisor = 2
    while divisor <= lowerOrder / 2:
        if lowerOrder%divisor == 0:
            isPrime = False
            break
        divisor = divisor + 1

    if isPrime:
        count = count + 1

        print(format(lowerOrder, "4d"), end="")
        if count % numPerLine == 0:
            print()

    lowerOrder = lowerOrder + 1
