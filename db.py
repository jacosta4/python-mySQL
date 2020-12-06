import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'guest_user',
    password = 'password1234',
    database = 'my_community'
)

cursor = mydb.cursor()

def create_user(username, first_name, last_name, age, email, country):
    sql = """
        INSERT INTO users (username, first_name, last_name,
        age, email, country)
        VALUES (%s, %s, %s, %s, %s, %s )"""
    values = (username, first_name, last_name, age, email, country)
    cursor.execute(sql, values)
    mydb.commit()

    # mydb.close()
