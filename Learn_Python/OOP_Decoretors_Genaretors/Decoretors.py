''' decoretors is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
'''

def my_decoretor(func):
     def my_func(*args, **kwargs):
          return func(*args, **kwargs)
     return my_func
@my_decoretor
def test(func):
     func = input('enter your name: '), input('enter your age: ')
     return f"hello world, my name is {func}"

test()

