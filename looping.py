import random
import os
import sys

# for x in range(0,10): # to not incl. 10
#     print(x, ' ', end='')

# grocList=["Apples", "Bread", "Cheese", "Donuts", "Eggs"]
# for y in grocList:
#     print(y)

# for x in [2,4,6,8]:
#     print(x)

# numList=[[1,2,3],[10,20,30],[100,200,300]]
# for z in range(0,3):
#     for zz in range(0,3):
#         print(numList[z][zz])

randomNum=random.randrange(0,100)

while(randomNum != 15):
    print(randomNum)
    randomNum=random.randrange(0,100)

