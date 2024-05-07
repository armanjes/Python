#🎁 Method 

#🚀 we call function as method inside a class

class myClass:
    year = 2020
    # every method takes self as first parameter which refers to the instance of the class, allowing methods to access and modify instance properties.
    def myMethod(self):
        print("this is a method")
        print(self.year)

myObj = myClass()
print(myObj.year)
myObj.myMethod()