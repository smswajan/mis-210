total_occupied = 0
for floor in range(10, 17):
    if floor == 13:
        continue
    num_of_suits = int(input("How many suits are occupied in floor {0} : ".format(floor)))
    if num_of_suits not in range(0, 21):
        num_of_suits = int(input("Enter the value between 0 and 20 : ".format(floor)))
    total_occupied = total_occupied + num_of_suits
print("The total number of suits occupied =", total_occupied)

total_suits = 120
percent_of_occupancy = total_occupied * 100 / total_suits
print("The hotel has {0} suits, {1} of those are occupied. The percentage of them are occupied is {2}".format(total_suits,total_occupied,percent_of_occupancy))
