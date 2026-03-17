# INTEGERS:

my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))
print(type(my_int_2))

#addition of integers

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints) #Integer addition: 68

#subtraction of ints
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints) # Integer Subtraction: 44

#multiplication
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)

#division
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1/my_int_2
print('Integer Division:', div_ints)

#FLOATS:

my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))
print(type(my_float_2))

#addition of floats
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition)

#subtraction
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction)

#multiplication
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication)

#division
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division)

#addition of a float and integer
my_int = 56
my_float = 5.4
sum_int_and_float = my_int + my_float

print(sum_int_and_float)
print(type(sum_int_and_float))

#modulo 
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats)

#floor division
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) 
print('Float Floor Division:', floor_div_floats)

#exponentiation
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12

exp_ints = my_int_1 ** my_int_2 
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation: ', exp_ints)
print('Float Exponentiation: ', exp_floats)

#float() function
my_int_1 = 56
my_float_1 = float(my_int_1)
print(my_float_1)
print(type(my_float_1))
