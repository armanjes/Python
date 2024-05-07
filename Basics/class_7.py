#🎁 Introduction to python List


# ✅ List is known as array in other programming languages. We create a list in python using "[]", this is an empty list. Lists can be stored in a variable and we can assign values (any data type together) in it separated by comma. 

firstList = ["xyz", 1200, 12.6, True]
print(firstList)    #output: ['xyz', 1200, 12.6, True]

print('\n')

# 🚀 We can access each value individually by its index. Index starts from 0 for the first element.

print(firstList[0])     #output: 'xyz'
print(firstList[2])     #output: 12.6
print(firstList[1])     #output: 1200

print('\n')

# 🚀 use len(List) method to know the length of a list. We can iterate over a list using loops.

for i in range(len(firstList)):
    print(f'Item at {i} index: {firstList[i]}')
    # Item at 0 index: xyz
    # Item at 1 index: 1200
    # Item at 2 index: 12.6
    # Item at 3 index: True
print('\n')

# 🚀 Lists are mutable means we can change its value.


firstList[0] = "linux"
print(firstList)    #output: ['linux', 1200, 12.6, True]
print('\n')


# ✅ Insert item in list

# append() -> method inserts item at the last.
fruits = ['mango', 'coconut', 'apple']
fruits.append('straw berry')
print(fruits)

# insert() -> method inserts an item at the specified index.
digits = [1, 2, 4]
digits.insert(2, 3)
print(digits)
print('\n')

# ✅ Deleting item from list

names = ['john', 'oggy', 'jack', 'bob']

# remove() -> method removes the specified item.
names.remove("oggy")
print(names)

# pop() -> method removes the specified index.
names.pop(1)
print(names)

# del -> keyword also removes the specified index
del names[0]
print(names)
print('\n')

# ✅ List operation

# Concat operation
evenList = [2,4,6,8,10]
oddList = [1,3,5,7,9]
newList = evenList + oddList
print(newList)

# Membership operation
print(2 in evenList)
print(2 in oddList)