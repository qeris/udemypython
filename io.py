import random
import sys
import os

testFile = open("test.txt", "wb")
print(testFile.mode)
print(testFile.name)

testFile.write(bytes("Write me to the file\n", "UTF-8"))
testFile.close()

testFile = open("test.txt", "r+")
testFile = testFile.read()

os.remove("test.txt")