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
    update = pyip.inputYesNo(prompt='Do want to see your data?(yes/no): \n')
    if update == 'yes':
        # print("Let's update some data")
        # update_choice = pyip.inputMenu(['username', 'first_name', 'last_name',
        #     'age', 'email', 'country'], numbered=True)
        # update_value = pyip.inputStr(f'Enter your new {update_choice}: ')
        # db.update_data(update_choice, update_value, username1)
        # funcion de actualizar
        # print('data updated')
        db.show_user(username1)
    else:
        print('Thank you, have a good day!')

print('\nThank you, have a good day!')


# Mostrar usuarios base de datos
# db.show_all_users()
