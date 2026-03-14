#String-seq of characters surrounded by either single or double quote marks.

my_str_1 = 'Hello'
my_str_2 = "World"
print(my_str_1, my_str_2)

#multiline string, use triple double quotes or single quotes

my_str_3 = """Multiline
string\n """
my_str_4 = '''Another multiline string'''
print(my_str_3, my_str_4)

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
print(msg, quote)

#to check whether a string contains one or more characters 

my_str = 'Hello world'

print('Hello' in my_str) #True
print('hey' in my_str) #False
print('hi' in my_str) #False
print('e' in my_str) #True
print('f' in my_str) #False

#Length of string and indexing

my_str = 'Hello world'
print(len(my_str))

#indexing
my_str = 'Hello world'

print(my_str[0]) #H
print(my_str[8]) #r

#neg indexing

print(my_str[-1]) #d

#immutable strings,you can reassign a diff string to a variable
greeting = 'hi'
greeting = 'hello'
print(greeting)

#string concatenation

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

#string + number

name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

#augmented assingnment operator

name = 'John Doe'
age = 26

name_and_age = name #start with the name
name_and_age += str(age) #Append the age as string

print(name_and_age) #John Doe26

#String interpolation(f string)

name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) #My name is John Doe nad I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') #The sum of 5 and 10 is 15

# String slicing

my_str = "Hello world"
print(my_str[1:4]) #ell

#omitting the start and stop indices

my_str = 'Hello world'
print(my_str[:7])

my_str = 'Hello world'
print(my_str[8:])

#common string methods, upper():

my_str = "hello world"
uppercase_my_str = my_str.upper()
print(uppercase_my_str)

#lower():

my_str = 'Hello World'
lowercase_my_str = my_str.lower()
print(lowercase_my_str)

#strip

my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"

#replace(old, new):

my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str) # hi world

# split(separator):

my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']

# join(iterable) :

my_list = ['hello', 'world']

joined_my_str = ''.join(my_list)
print(joined_my_str) # hello world

# startswith(prefix): 
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello) # True

# endswith(suffix):

my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world) # True

# find(substring):
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index) # 6


