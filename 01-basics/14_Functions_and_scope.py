# Functions are reusable pieces of code that run when you call them

#input()
name = input('What is your name?')
print('Hello', name)

#You can also write your custom functions - brgin with def keyword()
def hello():
    print('Hello World')

#simple function that prints the sum of two numbers.
def calculate_sum(a,b):
    print(a + b)

#calculating sum of two numbers
calculate_sum(3, 1)

#functions also use a special "return" keyword to exit the function and return a value.
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1)
print(my_sum)