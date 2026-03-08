''' this is a file handling program in python '''
from ipykernel.kernelapp import kernel_aliases

# opening a file in write mode
file = open('example.txt', 'r+') # opening a file in write mode
file.write('Hello, this is a file handling example in Python.\n') # writing to the file
file.write('We are learning how to handle files in Python.\n') # writing to the file
# file.close() # closing the file
print('File written successfully.')
m= file.read()
print(m)
open('myfile.txt', 'w').write('hello') # this will clear the contents of the file

with open('myfile.txt', 'r') as f:
     with open('myfile_copy.txt', 'w') as f_copy:
         for line in f:
             f_copy.write(line)
