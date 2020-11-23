import random
import os
import sys

age = 21

if age > 16 :
    print("You are old enough to drive")
else :
    print('You are not old enough')

if age >= 21 :
    print('You can drink')
elif age >= 16 :
    print("You can drive")
else : 
    print("You're not old enough")


if ((age >=1) and (age <= 18)):
    print("You get a bday")
elif age == 21 or age >=65:
    print("You get a bday too")
elif not(age ==30):
    print("You dont get a bday")
else:
    print("You get a party!")