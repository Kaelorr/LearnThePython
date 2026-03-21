''' Definition of functions for the conditions, loops, and functions practice.'''


def is_even():
    return'This function is not implemented yet.'

print(is_even().upper())

def is_odd(num):
    '''Returns True if num is odd, False otherwise.'''
    return num % 2 != 0

def is_factor(num, factor):
    '''Returns True if factor is a factor of num, False otherwise.'''
    return num % factor == 0

# .upper() , .lower() , .title() , .capitalize() , .swapcase() , .count() , .find() , .replace() , .strip() , .lstrip() , .rstrip() , .startswith() , .endswith() , .split() , .join() , .format() , f-strings, .isalpha() , .isdigit() , .isspace() , .isupper() , .islower() , .istitle() , .isnumeric() , .isdecimal() , .isidentifier() , .isprintable() , .isinstance() , .len() , .range() , .enumerate() , .zip() , .map() , .filter() , .reduce()  , lambda functions, list comprehensions, generator expressions, and more can be used in the practice exercises.


def main():
    print(is_odd(3))  # True
    print(is_odd(4))  # False
    print(is_factor(10, 2))  # True
    print(is_factor(10, 3))  # False


def test (*args,**kwargs):
    print(args)
    print(kwargs)

test(1, 2, 3, name='Corey', age=30)


def leap_year(year):
    '''Returns True if year is a leap year, False otherwise.'''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def factorial(n):
    '''Returns the factorial of n.'''
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


