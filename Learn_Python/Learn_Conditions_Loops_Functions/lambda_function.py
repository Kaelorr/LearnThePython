'''
Definition of lambda function is an anonymous function that can have any number of arguments but only one expression. 
It is often used for short, simple functions that are not reused elsewhere in the code.
The syntax for a lambda function is: lambda arguments: expression
work of some built-in functions with lambda functions, shortly described here:
1. filter(): The filter() function is used to filter elements from a sequence (like a list) based on a condition defined in a lambda function. 
It returns an iterator that contains only the elements that satisfy the condition.
2. map(): The map() function applies a given function (like a lambda function) to each item of an iterable (like a list) and returns an iterator with the results.
3. sorted(): The sorted() function can take a lambda function as the key argument to specify a custom sorting order. 
The lambda function defines the sorting criteria based on the elements of the iterable.
4. Conditional expressions: Lambda functions can also include conditional expressions (using the if-else syntax) to return different values based on certain conditions.
 This allows for more complex logic within a single line of code. 
For example, a lambda function that checks if a number is even or odd can be written as:
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(4))  # Output: Even
print(check_even_odd(5))  # Output: Odd'''

# Example of a lambda function that adds two numbers:
add = lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8

# Example of a lambda function that squares a number:
square = lambda x: x**2
print(square(4))  # Output: 16

# Using lambda with filter() to get even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Using lambda with map() to double all items in a list:
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Using lambda with sorted() to sort a list of tuples by the second element:
points = [(1, 2), (3, 1), (5, -1), (0, 4)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)  # Output: [(5, -1), (3, 1), (1, 2), (0, 4)]

# Conditional expression in lambda:
check_limit = lambda x: "High" if x > 10 else "Low"
print(check_limit(15))  # Output: High
print(check_limit(5))   # Output: Low