# Taking inputs for subtotal & gratuity
subtotal = eval(input("Enter the subtotal : "))
gRate = eval(input("Enter a gratuity rate: "))

# Calculating gratuity
gratuity = subtotal * gRate / 100

# Calculating total
total = subtotal + gratuity

# Now it's time to print out the result
print("The gratuity is", gratuity, "and the total is", round(total, 2))
