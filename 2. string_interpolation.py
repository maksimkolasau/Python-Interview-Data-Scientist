name = 'Chris'

# 1. f strings
print(f'Hello {name}')
print(f'Hi my name is {name}')

# 2. % operator
print('Hey %s' % name)

name_2 = 'Maksim'
age = 32
print('Hello, my name is %s, I am %d years old!' % (name_2, age))
print('Hi, I am %s' % name)
print('Give me please apple, %s' % name_2)

# 3. format
print("My name is {}".format(name))
print('My name is {}, and I have {} million dollars'.format(name_2, age))


