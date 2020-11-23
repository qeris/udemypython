import random
import sys
import os

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart'}

print(super_villains['Captain Cold'])

del(super_villains['Fiddler'])

print(len(super_villains))
print(super_villains.get("Captain Cold"))
print(super_villains.keys())
print(super_villains.values())