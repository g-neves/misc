#!/usr/bin/env python3

import abc


class AnimalInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_genus(self):
        """Returns the genus of the animal"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_species(self):
        """Returns the species of the animal"""
        raise NotImplementedError

class Dog(AnimalInterface):
    """Class that represents a dog"""
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def get_genus(self) -> str:
        """Returns the genus of the dog"""
        return "Canis" 

    def get_species(self) -> str:
        """Returns the species of the dog"""
        return "Canis familiaris" 

    def __str__(self):
        return f"{self.name} is a {self.get_species()} and is {self.age} years old."

class Cat(AnimalInterface):
    """Class that represents a cat"""

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def get_genus(self) -> str:
        """Returns the genus of the cat"""
        return "Felis" 

    def get_species(self) -> str:
        """Returns the species of the cat"""
        return "Felis catus" 

    def __str__(self):
        return f"{self.name} is a {self.get_species()} and is {self.age} years old."


if __name__ == "__main__":
    tica = Dog("Tica", 4)
    ozzy = Cat("Ozzy", 6)

    print(tica)
    print(ozzy)
