#🎁 Introduction variables

"""
Python is dynamically typed language. Means we don't need to specify the data of the variable. Python is a case sensitive language that means same variable name in different case is are different. Python treats them as different.
"""

#🚀 Assigning integer value to a variable
age = 25

#🚀 Assigning float value to a variable
temperature = 98.6

#🚀 Assigning string value to a variable
name = "John Doe"   # 'John Doe'

#🚀 Assigning values to multiple variables in a single line
x, y, z = 10, 20, 30

#🚀 Reassigning variables
_a = 5      # x is 5
_a = 10     # x is now 10 (previous value is overwritten)

#🎁 Introduction to data types

"""
🚀 there are 5 standard data types 
    1. Number (int, float, long, complex)
    2. String (anything inside "" or '' is a string)
    3. List 
    4. Tuple 
    5. Dictionary
    
🚀 we use type() function to check data type
"""


x = 5
print(type(x))  # Output: <class 'int'>

y = 3.14
print(type(y))  # Output: <class 'float'>

name = "John"
print(type(name))  # Output: <class 'str'>

lst = [1, 2, 3]
print(type(lst))  # Output: <class 'list'>

my_tuple = (1, 2, 'a', 'b', True)
print(type(my_tuple))   # Output: <class 'tuple'>

d = {'a': 1, 'b': 2}
print(type(d))      # Output: <class 'dict'>

print(type(True))   # Output: <class 'bool'>

set = {1,2,3,4,5}
print(type(set))    # Output: <class 'set'>

# Custom data type example
class MyClass:
    pass

obj = MyClass()
print(type(obj))  # Output: <class '__main__.MyClass'>


#🎁 Introduction to comments

# this is a single line comment

'''
this is a 
multiline comment.
'''