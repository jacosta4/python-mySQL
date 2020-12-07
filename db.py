import mysql.connector
import pyFuncs

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'guest_user',
    password = 'password1234',
    database = 'my_community'
)

cursor = mydb.cursor(dictionary=True)

def create_user(username, first_name, last_name, age, email, country, join_date):
    sql = """
        INSERT INTO users (username, first_name, last_name,
        age, email, country, join_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s )"""
    values = (username, first_name, last_name, age, email, country, join_date)
    cursor.execute(sql, values)
    mydb.commit()

    mydb.close()

def show_all_users():
    query = """
            SELECT user_ID, username, join_date
            FROM users
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    mydb.commit()
    mydb.close()

# buscar username en db
def search_username(username1):
    query = """
            SELECT username
            FROM users
            WHERE username = %s
            """
    value = (username1,)
    cursor.execute(query,value)
    data = cursor.fetchall()
    if len(data) == 0:
        return f"Username dont exists"
    else:
        return f"Username already exists"
    mydb.commit()
    mydb.close()
