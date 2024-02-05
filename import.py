import math
import random
firstNum=float(input('Write a Float number:'))
floorNum=math.floor(firstNum)
secondNum=float(input('Write a Float number bigger than first one:'))
print("Your first number rounded down to nearest integer, your second number also rounded up to nearest integer")
ceilNum=math.ceil(secondNum)
print("Now you'll get a random integer between ", floorNum, ' and ' , ceilNum)

print("You recieved:", random.randint(floorNum, ceilNum))