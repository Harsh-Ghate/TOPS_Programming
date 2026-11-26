"""

An abstract class in Python is a blueprint class that cannot be instantiated on its own and requires subclass to implement specific methods. You create
one using Python's built-in (abc) module by inheriting from ABC and decorating methods with @abstractmethod

from ab import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
    
# animal = Animal() # Raises: TypeError we can not declare abstract class object
"""

from abc import ABC, abstractclassmethod

class Animal(ABC):

    @abstractclassmethod
    def sound(self):
        pass
    def walk(self):
        pass

# animal = Animal() #Raises TypeError we can not declare abstract class object 

class Dog(Animal):
    def sound(self):
        return "Bark"

dog = Dog()
print(dog.sound)