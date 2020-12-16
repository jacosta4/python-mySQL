import datetime
import pyinputplus as pyip

def get_date():
    date = datetime.datetime.now()
    return (f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}")

def create_user_data():
    username = pyip.inputStr(prompt='Username: ')
    first_name = pyip.inputStr(prompt='First Name: ')
    last_name = pyip.inputStr(prompt='Last Name: ')
    age = pyip.inputInt(prompt='Age: ', min=1, max=99)
    email = pyip.inputEmail(prompt='Email: ', )
    country = pyip.inputStr(prompt='Country: ')
    join_date = get_date()
    return username, first_name, last_name, age, email, country, join_date
