# 🎁 polymorphism

# 🚀 polymorphism means many forms. That means a method has many forms.


class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return "some cat sound..."
    
class Bird(Animal):
    def sound(self):
        return "some bird sound..."
    
cat = Cat()
print(cat.sound())

bird = Bird()
print(bird.sound())

# 🚀 Here sound method behaving differently in different class.