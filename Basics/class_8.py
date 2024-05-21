#🎁 Introduction to python Tuple

# ✅ Tuple is another data type in python. We create a tuple in python using parentheses "()", this is an empty tuple. Tuple can be stored in a variable and we can assign values (any data type together) in it separated by comma which starts form index 0. 

tuple1 = ('physics', 'chemistry', 1997, 15.05)
tuple2 = ()

# 🚀 When you define a tuple with a single element in Python, you need to include a comma after the element to distinguish it from a regular parenthesis-enclosed value. Without the comma, the expression (1404) is simply an integer enclosed in parentheses and not a tuple 

tuple3 = (1404,)

# 🚀 Tuple is immutable means you can't assign or delete any value, faster and consumes less memory.


# ✅ Unpacking tuple

# 🚀 When we create a tuple, we normally assign values to it. This is called "packing" a tuple. But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".

fruits = ("apple", "banana", "cherry")

(val1, val2, val3) = fruits

print(val1)     #output: apple
print(val2)     #output: banana
print(val3)     #output: cherry

# 🚀 The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

numbers = (1,2,3,4,5,6,7,8,9,10)
(val1, val2, *val3, val4) = numbers

print(val1)     #output: 1
print(val2)     #output: 2
print(val3)     #output: [3, 4, 5, 6, 7, 8, 9]
print(val4)     #output: 10