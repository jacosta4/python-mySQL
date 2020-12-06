import pyinputplus as pyip
import db

print('-- WELCOME!!--')
print('\nEnter the following data')

username = pyip.inputStr(prompt='Username: ')
first_name = pyip.inputStr(prompt='First Name: ')
last_name = pyip.inputStr(prompt='Last Name: ')
age = pyip.inputInt(prompt='Age: ', min=1, max=99)
email = pyip.inputEmail(prompt='Email: ', )
country = pyip.inputStr(prompt='Country: ')

# Guardar en DB los datos ingresados
db.create_user(username, first_name, last_name, age, email, country)
print('\nUser created successfully')
