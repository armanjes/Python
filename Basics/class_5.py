#🎁 Python Loops

'''
🚀 Python provides two primary types of loops for iterative tasks: for loop and while loop. 

🚀 range() is function that is used when using a for...loop for times. It takes minimum one parameter to maximum three parameter.
-> one parameter indicates ending and by default it starts with 0
-> two parameter indicates first one is the starting and second one ending
-> three parameter indicates that the third one is step size
'''

#✅ for...loop

for i in range(10):
    print(i)    # output: 0-9

print("\n")

for i in range(1, 11):
    print(i)    #output: 1-10

print("\n")

for i in range(1, 11, 2):
    print(i)    #output: odd numbers

print("\n")

#✅ while...loop
        
i = 1
while i < 11:
    print(i)    #output: 1-10
    i += 1

print("\n")

#✅ pass, break, continue keyword
        
for i in range(1, 11):
    if(i == 5):
        pass    # pass does nothing
    print(i)

print('\n')

for i in range(1, 11):
    if(i == 5):
        continue    # Skips the number 5
    print(i)

print('\n')

for i in range(1, 11):
    if(i == 5):
        break    # Stops executing the loop at 5
    print(i)