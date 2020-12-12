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
    ## ***** se puede hacer una funcion aca ******
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

    exists_choice = pyip.inputMenu(['Show your data', 'Update', 'Delete'],
            lettered=True)

    # Update data
    if exists_choice == 'update':
        print("Let's update some data")
        update_choice = pyip.inputMenu(['username', 'first_name', 'last_name',
            'age', 'email', 'country'], numbered=True)
        update_value = pyip.inputStr(f'Enter your new {update_choice}: ')
        if update_choice == 'username':
            db.update_data_username(update_value, username1)
            print('data updated')
        elif update_choice == 'first_name':
            db.update_data_first_name(update_value, username1)
            print('data updated')
        elif update_choice == 'first_name':
            db.update_data_last_name(update_value, username1)
            print('data updated')
        elif update_choice == 'first_name':
            db.update_data_age(update_value, username1)
            print('data updated')
        elif update_choice == 'first_name':
            db.update_data_email(update_value, username1)
            print('data updated')
        elif update_choice == 'first_name':
            db.update_data_country(update_value, username1)
            print('data updated')

    # Show user data
    elif exists_choice == 'Show your data':
        db.show_user(username1)

    # Delete user data
    elif exists_choice == 'Delete':
        delete_user = pyip.inputYesNo(prompt='Are you sure?(yes/no): \n')
        if delete_user == 'yes':
            db.delete_user(username1)
            print('User deleted.')
        else:
            print('Uff, so close!')


print('\nThank you, have a good day!')


# Mostrar usuarios base de datos
# db.show_all_users()
