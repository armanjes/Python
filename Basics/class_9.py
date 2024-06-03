#🎁 Introduction to python Set

#✅ A set is a collection which is unordered, unchangeable, unindexed and do not allow duplicate values. Sets are particularly useful for membership testing, removing duplicates from a sequence, and mathematical operations like union, intersection, difference, and symmetric difference.

#🚀 Set items are unchangeable, but you can remove items and add new items.

#✅ Creating Sets

#🚀 You can create a set by using the `set()` constructor or by placing elements inside curly braces `{}`.

#🚀 Using the set() constructor
set_a = set([1, 2, 3, 4])

#🚀 Using curly braces
set_b = {1, 2, 3, 4}

#🚀 Note that to create an empty set, you must use `set()` because `{}` creates an empty dictionary.

#🚀 Correct way to create an empty set
empty_set = set()

#🚀 This creates an empty dictionary, not a set
empty_dict = {}

#✅ Basic Operations

#🚀 Adding elements: `add()` method inserts an element at last.

set_a = {1, 2, 3}
set_a.add(4)    # set_a is now {1, 2, 3, 4}

#🚀 Removing elements: Use the `remove()` or `discard()` methods.

set_a.remove(2)  # Raises KeyError if 2 is not in the set
set_a.discard(3) # Does not raise an error if 3 is not in the set

#🚀 Checking membership: Use the `in` keyword.

1 in set_a  # Returns True
5 in set_a  # Returns False


#🚀 Set length: Use the `len()` function.
  
len(set_a)  # Returns the number of elements in set_a

#✅ Set Operations

#🚀 Union: Combines elements from both sets.

set_c = {1, 2, 3}
set_d = {3, 4, 5}
union_set = set_c | set_d  # {1, 2, 3, 4, 5}
union_set = set_c.union(set_d)  # Same result

#🚀 Intersection: Elements common to both sets.

intersection_set = set_c & set_d  # {3}
intersection_set = set_c.intersection(set_d)  # Same result

#🚀 Difference: Elements in the first set but not in the second.

difference_set = set_c - set_d  # {1, 2}
difference_set = set_c.difference(set_d)  # Same result

#🚀 Symmetric Difference: Elements in either set but not in both.

symmetric_difference_set = set_c ^ set_d  # {1, 2, 4, 5}
symmetric_difference_set = set_c.symmetric_difference(set_d)  # Same result

#🚀 Sets are a powerful tool in Python for managing collections of unique elements and performing common mathematical operations efficiently.