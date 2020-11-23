import random
import sys
import os


class Animal:
    # prepending double underscore __ to a name makes it private
    name = ""
    height = 0
    weight = 0
    sound = ""

    # Constructor
    def __init__(self, name, height, weight, sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setWeight(self, weight):
        self.weight = weight

    def getWeight(self):
        return self.weight

    def setSound(self, sound):
        self.sound = sound

    def getSound(self):
        return self.sound

    def getType(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kgs and says {}".format(self.name,
                                                                self.height,
                                                                self.weight,
                                                                self.sound)


class Dog(Animal):
    owner = ""

    def __init__(self, name, height, weight, sound, owner):
        super().__init__(name, height, weight, sound)
        self.owner = owner

    def setOwner(self, owner):
        self.owner = owner

    def getOwner(self):
        return self.owner

    def getType(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kgs and says {}. Their owner is {}".format(self.name,  # <-- Breaks here
                                                                                   self.height,
                                                                                   self.weight,
                                                                                   self.sound,
                                                                                   self.owner)

    def multipleSounds(self, amount=None):
        if amount is None:
            print(self.getSound)
        else:
            print(self.getSound() * amount)


cat = Animal("Impi", 33, 5, "Meow")
print(cat.toString())
giggle = Dog("Giggle", 10, 4, "Bark", "Ethan")
print(giggle.toString())
