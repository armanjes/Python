# 🎁 Introduction to Python Dictionary

'''
✅ Dictionary is another data type in Python.
That is used to store data in key-value pairs.
The key is any meaningful name enclosed with quotes, and
the value can be any valid data type including another dictionary in Python.
Every key-value pair is known as an item.
Every item is separated by ",".
We use "{}" for making a dictionary or we can use the "dict()" constructor.
'''

# 🚀 Empty dictionary
emptyDictionary = {}
# emptyDictionary = dict()
print(emptyDictionary)  # output: {}
print(len(emptyDictionary))  # output: 0
print(type(emptyDictionary))  # output: <class 'dict'>

# 🚀 Dictionary with values
thisDict = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1964,
}

print(thisDict)  # output: {'brand': 'Ford', 'model': 'mustang', 'year': 1964}

'''
🚀 Dictionary is ordered, changeable.
Dictionary doesn't allow key duplicates.
If you do so, it will overwrite the last key.
'''

myMarks = {
    'Bangla': 70,
    'English': 80,
    'Math': 85,
    'Math': 90
}
print(myMarks)  # output: {'Bangla': 70, 'English': 80, 'Math': 90}

# ✅ Accessing values

'''
🚀 Accessing values in a dictionary is similar to lists.
We use a key to access any value from a dictionary like
we use to do in lists using an index.
'''

studentInfo = {
    'Name': 'xyz',
    'Department': 'CSE',
    'University': 'NSU',
    'Roll no': 111111
}

print(studentInfo['Name'])  # output: xyz
print(studentInfo['Department'])  # output: CSE
print(studentInfo['University'])  # output: NSU

# 🚀 The keys() method will return a "list" of all the keys in the dictionary.
print(studentInfo.keys())

# 🚀 The values() method will return a "list" of all the values in the dictionary.
print(studentInfo.values())

# 🚀 The items() method will return each item in a dictionary, as tuples in a list.
print(studentInfo.items())

# ✅ Adding values in a dictionary

# 🚀 You can change the value of a specific item by referring to its key name.
countryCodeDict = {
    'India': 91,
    'UK': 44,
    'USA': 1,
    'Spain': 34
}

print(f'Before change: {countryCodeDict["India"]}')

countryCodeDict['India'] = 0
print(f'After change: {countryCodeDict["India"]}')

# 🚀 The update() method will update the dictionary with the items from the given argument. The argument must be a dictionary.

print(f'Before update: {countryCodeDict}')

countryCodeDict.update({'Bangladesh': 88})
print(f'After update: {countryCodeDict}')

# ✅ Removing values from a dictionary

# 🚀 The pop() method removes the item with the specified key name.

carDict = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1964,
    'fuel': 'Diesel'
}

print(f'Before pop: {carDict}')

carDict.pop('year')
print(f'After pop: {carDict}')

# 🚀 The popitem() removes the last item

print(f'Before popitem: {carDict}')

carDict.popitem()
print(f'After popitem: {carDict}')

# 🚀 The clear() method removes all the items from the dictionary and makes an empty dictionary

print(f'Before clear: {carDict}')

carDict.clear()
print(f'After clear: {carDict}')

# 🚀 del keyword is used to delete a dictionary.

del carDict
# The following line will raise an error because carDict is deleted
# print(carDict)

# ✅ Looping in a dictionary

personDict = {
    'Name': 'jon',
    'age': 28,
    'married': True,
    'post code': 5555
}

for i in personDict:
    print(i)  # prints keys
    print(personDict[i])  # prints values
    print(f'{i}: {personDict[i]}')

# ✅ Nested dictionary and looping

# 🚀 Nested dictionary
child1 = {
    'age': 5,
    'birth year': 2000
}

child2 = {
    'age': 10,
    'birth year': 2010
}

child3 = {
    'age': 20,
    'birth year': 2020
}

childDict = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}

print(childDict)
print(childDict['child1']['age'])
print(childDict['child2']['birth year'])

# 🚀 Nested dictionary looping
for i in childDict:
    print(i)
    print(childDict[i]['age'])
