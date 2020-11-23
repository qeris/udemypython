import random
import os
import sys

numbers = [1,2,3,4,5]
print(numbers[0])
numbers[2] = "three"
print(numbers)
print(numbers[1:3]) # not including 3

moreNumbers = [6,7,8,9,0]
allNumbers = [numbers, moreNumbers]
print(allNumbers[1][2])

numbers.append("ten")
print(numbers)
numbers.insert(1, 1.5)
print(numbers)
numbers.remove('ten')
print(numbers)