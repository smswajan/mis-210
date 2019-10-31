demand = eval(input("Demand Rate (i.e., 16,000 units): "))
setup_cost = eval(input("The setup cost is (i.e., BDT 50: "))
holding_cost = eval(input("The holding cost per item (i.e., BDT 2.5): "))

eoq = ((2 * demand * setup_cost)/holding_cost)**0.5
print("According to the provided data the EOQ is:", eoq)
