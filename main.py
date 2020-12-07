import pyinputplus as pyip
import db
import pyFuncs

print('\n-- WELCOME!!--')
print('\nEnter your Username please')

username1 = pyip.inputStr(prompt='Username: ')
user_vali = db.search_username(username1)
if user_vali == 'Username dont exists':
    print(f"Username dont exists, we're going to create your profile!")
    print('\nEnter the following data')
    username = pyip.inputStr(prompt='Username: ')
    first_name = pyip.inputStr(prompt='First Name: ')
    last_name = pyip.inputStr(prompt='Last Name: ')
    age = pyip.inputInt(prompt='Age: ', min=1, max=99)
    email = pyip.inputEmail(prompt='Email: ', )
    country = pyip.inputStr(prompt='Country: ')
    join_date = pyFuncs.get_date()

    #Guardar en DB los datos ingresados
    db.create_user(username, first_name, last_name, age, email, country, join_date)
    print('\nUser created successfully')
else:
    print('User exits')


# Mostrar usuarios base de datos
# db.show_all_users()
