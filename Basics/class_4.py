#🎁 Introduction to python conditionals

'''
🚀 if, if...else, if...elif...else
'''
#✅ if
def check1():
    number = int(input("enter a number: ")) #input() function for taking input()
    if number > 5: print(f'{number} is greater than 5')

check1()

#✅ if...else
def check2():
    number = int(input("enter a number: "))
    if number > 5: 
        print(f'{number} is greater than 5')
    else: 
        print(f'{number} is less than 5')

check2()

#✅ if...elif...else

def check3():
    name = str(input("Enter your name: ").strip().lower())
    if(name == 'abc'): 
        return f'Welcome {name}!'
    elif(name == 'xyz'):
        return f'Thank you {name}!'
    elif(not name):
        return 'Enter a name...'
    else:
        return f"Bot doesn't recognize {name}"

print(check3())

#🎁 Ternary conditional operator
'''Ternary operator is the short form what we did above.'''

#✅ if...else
def binary(a):
    return True if(a == 1 or a == 0) else False

print(binary(10))

#✅ if...elif...else
def evenOdd(n):
    return 'even' if(n % 2 == 0) else('zero' if(n==0) else 'odd')

print(evenOdd(5))
