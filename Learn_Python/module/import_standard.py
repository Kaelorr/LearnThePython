''' This file demonstrates importing standard Python modules. Definitions of functions for the importing standard modules practice. '''

# we can import lybraries from other files in the same directory or from standard library or from third party libraries.
# i can make multiple modules whichh i will used to multiple works. thats an very important thing to do.
#  it will make my code more organized and reusable. i can import the module in any file and use the functions defined in that module.
# import works_module

# import math as m # we can import a module with an alias. it will make our code more concise and easier to read. we can use the alias to access the functions defined in the module.

# we can import specific functions from a module. it will make our code more concise and easier to read. we can use the functions directly without the module name.
# from works_module import leap_year, factorial 


import sys 
print(sys.version) # it will print the version of python we are using. it is important to know the version of python we are using because some functions and features are only available in certain versions of python.
print(sys.platform) # it will print the platform we are using.
import math
print(math.pi) # it will print the value of pi.
print(math.sqrt(16)) # it will print the square root of 16.
print(math.factorial(5)) # it will print the factorial of 5.
import os
print(os.getcwd()) # it will print the current working directory.
import random as r
print(r.randint(1, 10)) # it will print a random integer between 1 and 10.
print(r.choice(['apple', 'banana', 'cherry'])) # it will print a random choice from the list.
print(r.random()) # it will print a random float between 0 and 1.
import datetime
print(datetime.datetime.now()) # it will print the current date and time.
print(datetime.date.today()) # it will print the current date.
import calendar
print(calendar.month(2024, 6)) # it will print the calendar for June 2024.
print(calendar.isleap(2024)) # it will print True if 2024 is a leap year, False otherwise
print(calendar.weekday(2024, 6, 1)) # it will print the weekday of June 1, 2024. (0: Monday, 1: Tuesday, ..., 6: Sunday)
import time
print(time.time()) # it will print the current time in seconds since the epoch. 
print(time.ctime()) # it will print the current time in a human-readable format.
print(time.sleep(5)) # it will pause the program for 5 seconds.
