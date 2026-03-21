# All concepts of python in details:
### 1. Basics of python-
(1. variables, 2. basic data types(str, int, bool, float), 3. user input, 4. comments, etc... )
### 2. Data types - list, tuples, dictionary, set..
### 3. conditionals - if-else-elif
### 4. loops - for loops, while loops, until loops
### 5. Functions
### 6. OOP - inheritance, polymorphism, encapsulation, insistence
### 7. Decoretors
### 8. Genaretors
### 9. File Handling
### Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
### Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
### 10. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")
finally:
    print("Execution completed.")

### 13. Lambda Functions
square = lambda x: x * x
print(square(5))

### 14. List Comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
### 15. Modules and Packages
import math
print(math.sqrt(16))

### 16. Working with JSON
import json
data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)
print(json_string)

### 17. Regular Expressions
import re
text = "The rain in Spain"
match = re.search("^The.*Spain$", text)
if match:
    print("Match found!")

### 18. Iterators
my_list = [1, 2, 3]
my_iter = iter(my_list)
print(next(my_iter))
print(next(my_iter))

### 19. Closures
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Hi")
hi_func()

### 20. Args and Kwargs
def my_function(*args, **kwargs):
    print(args)
    print(kwargs)

my_function(1, 2, 3, name="John", age=30)
### 21. Context Managers
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

with MyContext():
    print("Inside the context")

### 22. Enumeration
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

### 23. Zip Function
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

### 24. Shallow vs Deep Copy
import copy
original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

### 25. Multithreading and Multiprocessing
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()



