# 🎁 method overloading

# 🚀 Multiple method with same name but different parameters is know as method overloading. There signature may be different. Python doesn't support this feature of OOP but we can achieve this by some tricks.

class MyClass:
    def my_method(self, x=None):
        if x is None:
            return 'x is empty.'
        elif isinstance(x, int):
            return f'x has an integer value: {x}'
        elif isinstance(x, str):
            return f'x has an string value: {x}'
        else:
            return f'x has an float value: {x}'

obj = MyClass()
print(obj.my_method())
print(obj.my_method('abc'))
print(obj.my_method(25))
print(obj.my_method(3.65))

# 🚀 is is used to check if x is None.
# 🚀 isinstance(x, int) is used to check if x is an instance of the int, float or string class.
