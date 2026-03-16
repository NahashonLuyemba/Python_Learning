first_name = 'John'
last_name = "Doe"


full_name = first_name + ' ' + last_name # added space between two names
print(full_name)

address = '123 Main Street'
address += ', Apartment 4B'
print(address)

employee_age = 28
employee_info = full_name + " is " + str(employee_age)
employee_info += ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

full_name = 'John Doe'
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)
