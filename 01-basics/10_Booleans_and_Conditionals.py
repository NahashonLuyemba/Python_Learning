# comparison operators
print(3 > 4)
print(3 < 4)
print(3 == 4)
print(4 == 4)
print(3 != 4)
print(3 >= 4)
print(3 <= 4)

#if statement
age = 12

if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet')

#multiple conditions
age = 12
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')


#2
age = 12

if age >= 65:
    print('You are asenoir ctizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >=  13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant')

# nested conditionals 
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You area eligible to vote')

else:
    print('You are not eligible to vote')        



