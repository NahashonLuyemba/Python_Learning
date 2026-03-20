#And
is_citizen = True
age = 25

print(is_citizen and age)

#instead of nested if ststements
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

# 'or' operator
age = 19
is_employed = False

print(age or is_employed)
 
#to check if one or more operations is True 
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount')
else:
    print('You are not eligible for a student discount')
    
        

