# 🎁 Inheritance

# 🚀 Inheritance is a process where you access the properties of a super class from sub class. Inheritance allows to reuse code. There are mainly three types of inheritance.

# 🚀 single inheritance
class A:
    def feature1(self):
        return 'this is feature 1.'
    def feature2(self):
        return 'this is feature 2.'
    
class B(A):
    def feature3(self):
        return 'this is feature 3.'

b = B()
print(b.feature2()) # output: this is feature 2.

# 🚀 multilevel inheritance
class C(B):
    def feature4(self):
        return 'this is feature 4.'
    def feature5(self):
        return 'this is feature 5.'

c = C()
print(c.feature3()) # output: this is feature 3.

# 🚀 multiple inheritance
class D():
    def feature5(self):
        print("this is feature 5.")

class E(A, D):
    pass

e = E()
print(e.feature2()) # output: this is feature 2.
