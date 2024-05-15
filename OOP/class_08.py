# 🎁 Abstraction

# 🚀 A class with one or more abstract method is known as abstract class. A method without body or method with only declaration is know as abstract method. We can't make object of an abstract class and we must override abstract methods in subclass.

''' In Python we can't implement this feature directly. We have to use a module abc (abstract base class).
'''

from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def go(self):
        pass

