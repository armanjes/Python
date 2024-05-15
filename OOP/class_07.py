# 🎁 method overriding

# 🚀 Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. Which is similar like polymorphism. 

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Usage
animal = Animal()
animal.sound()  # Output: Generic animal sound

dog = Dog()
dog.sound()     # Output: Bark

cat = Cat()
cat.sound()     # Output: Meow

# 🚀 we must override the methods of superclass neither It will through an error