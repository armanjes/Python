#🎁 Function define

'''
🚀 Function is a block of code that completes any specific task and runs when it is called. We use "def" keyword for making function and function has name we call function with the name along with "()"
'''

def sayHello():
    print('hello...')

sayHello()


#✅ Function parameter 
'''
🚀 Function can receive values and return values. We pass value in it by parameters
'''

def sayHello(name):
    # name is a parameter.
    # We can pass multiple parameters
    return f'Hello, {name}.'

print(sayHello('arman'))    # here we passed 'arman' as an argument

'''
🚀 There are two types of functions 
        1. Pre-defined/ library functions
        2. User-defined functions

The function we made above are user-defined functions. We can store a function in a variable.
'''

#✅ Function nesting
'''
🚀 If we make function inside another function is known as function nesting. If we do nesting we must call child function inside parent function. The child function can take or we can pass values from parent to child function by the help of "Closure"
'''
def outer(x):
    print('this is outer function')
    def inner(x):
        return (f'this is inner function {x}')
    print(inner(x))

outer(True)

#✅ Lambda/ anonymous  Function
'''
🚀 Lambda function has no name thats why it's called anonymous and it is made with "lambda" keyword. We can store it in a variable. A lambda function can take any number of arguments, but can only have one expression.
''' 

lambdaFunction = lambda x,y :  x+y
print(lambdaFunction(10, 10))

#🎁 Python scope

'''
🚀 Scope refers to the region of a program where a particular variable is accessible. There are 4 scope in python.
'''

# ✅ Global scope
'''
🚀 Variable declared outside of a function are global function and we can access them form anywhere.
'''
x = 10
def getValueFromGlobal():
    print(x)
getValueFromGlobal()

# ✅ Local scope
'''
🚀  Variables defined within a function have local scope. We can't access them outside of the function
'''

def localScopeFunction():
    x = 100
    return x

result = localScopeFunction
print(result())

# ✅ Non-local scope
'''
🚀 This scope applies in nested functions. This happens due to "Closure"
'''

def outer(val):
    x = val
    def inner():
        return x * 2
    print(inner())

outer(50)

# ✅ Built-in scope
'''
🚀 This scope includes pre-defined function scope such as: print(), len(), str()
'''

#🎁 Python operators

#✅ Arithmetic Operators

# Addition
result = 10 + 5  # result = 15

# Subtraction
result = 10 - 5  # result = 5

# Multiplication
result = 10 * 5  # result = 50

# Division
result = 10 / 5  # result = 2.0 (float division)

# Modulus (remainder)
result = 10 % 3  # result = 1

# Exponentiation
result = 10 ** 2  # result = 100

#✅ Comparison Operators

# Equal to
result = 10 == 5  # result = False

# Not equal to
result = 10 != 5  # result = True

# Greater than
result = 10 > 5   # result = True

# Less than
result = 10 < 5   # result = False

# Greater than or equal to
result = 10 >= 5  # result = True

# Less than or equal to
result = 10 <= 5  # result = False

#✅ Logical Operators

# Logical AND
result = (10 > 5) and (5 < 3)  # result = False

# Logical OR
result = (10 > 5) or (5 < 3)   # result = True

# Logical NOT
result = not (10 > 5)          # result = False

#✅ Assignment Operators

# Simple assignment
x = 10

# Add and assign
x += 5  # Equivalent to x = x + 5

# Subtract and assign
x -= 3  # Equivalent to x = x - 3

# Multiply and assign
x *= 2  # Equivalent to x = x * 2

# Divide and assign
x /= 3  # Equivalent to x = x / 3

#✅ Identity Operators

x = [1, 2, 3]
y = [1, 2, 3]

# is
result = x is y   # result = False

# is not
result = x is not y  # result = True

#✅ Membership Operators

my_list = [1, 2, 3]

# in
result = 2 in my_list   # result = True

# not in
result = 4 not in my_list  # result = True
