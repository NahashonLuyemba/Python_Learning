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








