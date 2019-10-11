count = 1
for i in range (100, 1001):
  if i % 5 == 0 and i % 6 == 0:
    #ensuring that each line has a limited number of 10 numbers
    if count%10 == 0:
      print(format(i, "4d"))
    else:
      print(format(i, "4d"), end="")
    
    count += 1
