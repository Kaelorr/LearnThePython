''' This file is for learning about comprehension in python. '''


dict_ = {'a': 1, 'b': 2, 'c': 3}
# List comprehension
squared = [x**2 for x in range(10)]
print(squared)

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)

# Set comprehension 
squared_set = {x**2 for x in range(10)}
print(squared_set)

# Generator comprehension
squared_gen = (x**2 for x in range(10))
print(squared_gen)
for num in squared_gen:
    print(num)
# Nested comprehension
nested_list = [[x**2 for x in range(5)] for y in range(3)]
print(nested_list)