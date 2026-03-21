import os
# print(dir(os))# module ar all method to see, dir method use hoy
os.chdir(os.path.dirname(__file__))  # to change current path
# os.chdir('test')
print(os.getcwd()) # to see current working directory
os.listdir() # to see all of folder and directory in list
for file in os.listdir():
    print(file)
os.rmdir('test2')
os.mkdir('test') # to make new directory
os.rename('test', 'test2')
os.walk('test2')
print(os.environ.get('HOME'))
print(os.environ.get('USERPROFILE'))
print(os.path.join(os.environ.get('HOME'), 'test2.txt'))
os.path.isdevdrive()