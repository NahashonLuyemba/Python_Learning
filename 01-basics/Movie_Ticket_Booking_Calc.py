base_price = 15
age = 21

seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eiligble for Evening shows') 
else:
    print('User is not eligible for Evening shows') 

is_member = True
is_weekend = False

discount = 0
if is_member:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount) 

if is_member and age >= 21:
    print('User is eligible to membership discount and Evening shows')

extra_charges = 0
if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')

else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)

if is_weekend or show_time == 'Evening':
    if age >= 21:
        print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions') 

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3    
    else:
        service_charges = 1  
    print('Service charges:', service_charges)   



