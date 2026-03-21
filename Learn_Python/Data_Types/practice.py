#!/usr/bin/env python3

print('This is your data input station')

your_data = { "your_name": None, "your_age": None, "your_city": None }


def my_function():
    name = input(str("Please enter your name: "))
    your_data['your_name'] = name
    age = input(str("Please enter your age: "))
    your_data['your_age'] = age
    city = input(str("Please enter your city: "))
    your_data['your_city'] = city
    print('Thanks for providing your time')

# my_function()

# my_list = [1,  2,  3,  4,  5,  6,  7,  8,  9,  10]
#          0   1   2   3   4   5   6   7   8   9  ,10, -9, -8, -7, -6, -5, -4, -3, -2, -1
#        -10  -9  -8  -7  -6  -5  -4  -3  -2  -1  0
# print(my_list[-1:-11])
# print(my_list[-1:-11:-1])  # Use step -1 to reverse and get elements from last to first
# print(my_list[0:10:1]) # first 0 is the start index, second 10 is the stop index, and 1 is the step (forward order)
# print(my_list[-1:-11:-1]) # first -1 is the start index, second -11 is the stop index, and -1 is the step (reverse order)
# print(my_list[0:0:-1])  # This will return an empty list because the start and stop indices are the same
# # print(my_list[0:10:-1])
# print(my_list[2:8:2])  # This will return [3, 5, 7] (elements at indices 2, 4, and 6)
# print(my_list[0:10])  # This will return the entire list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] because the step is 1 (default)
# print(my_list[0:10:2])  # This will return [1, 3, 5, 7, 9] (elements at indices 0, 2, 4, 6, and 8)
# var = "Hello, World!"
# print(var[0:5])  # This will return 'Hello' (characters at indices 0 to 4)
# print(var[7:12])  # This will return 'World' (characters at indices 7 to 11)
# print(var[0:12:2])  # This will return 'Hlo ol!' (characters at indices 0, 2, 4, 6, 8, and 10)


# list comprehension example
# squares = [x**2 for x in range(1, 11)]
# print(squares)  # This will print the list of squares from 1 to 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print("Thank you for providing your data!")
# print("Now you can use this data for various purposes, such as creating a profile, analyzing trends, or sharing it with others.")


match 