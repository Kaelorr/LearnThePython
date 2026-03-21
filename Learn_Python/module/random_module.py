import random

list_=['Hello', 'Hi', 'hola', 'hey', 'world']
print(random.choice(list_))
print(random.choices(list_,weights=[18, 18, 1, 2, 19], k=10))
print(dir(random)) # that will print all methods in the random module
print(random.random()) # that will print random numbers
print(random.randint(1,1000)) # that will print random integer from the range
# print(random.gauss(1,10))
print(random.uniform(1,1000))  # that will print random float from the range
print(random.randrange(1,1000))
print(random.shuffle(list_))