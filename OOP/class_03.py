# 🎁 constructor method

# Constructor in python is a special method that is called when an object is created. The purpose of a python constructor is to assign values to the data members within the class when an object is initialized. The name of the constructor method is always __init__.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"name is: {self.name}")
        print(f'age is: {self.age}')

p1 = Person("xyz", 123)
p1.display()