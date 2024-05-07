#🎁 Introduction to python data type detection

#🚀 we use type() to check data type

# Define some variables with different data types
var_int = 10
var_float = 3.14
var_str = "Hello, World!"
var_list = [1, 2, 3, 4, 5]
var_dict = {"name": "John", "age": 30}
var_set = {1, 2, 3}
var_tuple = (1, 2, 3)
var_bool = True
# Custom data type example
class MyClass:
    pass

obj = MyClass()


# Check the type of each variable
print(type(var_int))    # Output: <class 'int'>
print(type(var_float))  # Output: <class 'float'>
print(type(var_str))    # Output: <class 'str'>
print(type(var_list))   # Output: <class 'list'>
print(type(var_dict))   # Output: <class 'dict'>
print(type(var_set))    # Output: <class 'set'>
print(type(var_tuple))  # Output: <class 'tuple'>
print(type(var_bool))   # Output: <class 'bool'>
print(type(obj))  # Output: <class '__main__.MyClass'>



#🎁 Introduction to python data type conversion

#🚀 perform data type conversion using built-in functions like int(), float(), str(), list(), dict(), set(), tuple() and bool().

num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10

num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14
print(int(num_float)) #output: 3

num_int = 10
num_str = str(num_int)
print(num_str)  # Output: '10'

num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(num_list)  # Output: [1, 2, 3]

num_list = [("a", 1), ("b", 2)]
num_dict = dict(num_list)
print(num_dict)  # Output: {'a': 1, 'b': 2}

num_list = [1, 2, 3, 3, 4]
num_set = set(num_list)
print(num_set)  # Output: {1, 2, 3, 4}

num_list = [1, 2, 3]
num_tuple = tuple(num_list)
print(num_tuple)  # Output: (1, 2, 3)

print(bool(1)) # Output: True

#🚀 gives false only in 0
print(bool(0)) # output: False