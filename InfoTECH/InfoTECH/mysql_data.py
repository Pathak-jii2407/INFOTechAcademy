import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ved24072003",
    database="infotechacademyrewa"
)
cursor = connection.cursor()

def save_data_to_mysql(new_data):
    try:
        name = new_data['name']
        phone = new_data['number']
        email = new_data['email']
        password = new_data['password']
        course = new_data['course']
        language = new_data['language']

        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            phone VARCHAR(255) UNIQUE,
            email VARCHAR(255),
            password VARCHAR(255),
            course VARCHAR(255),
            language VARCHAR(255)
        )
        """
        cursor.execute(create_table_query)

        insert_query = """
        INSERT INTO users (name, phone, email, password, course, language) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        data = (name, phone, email, password, course, language)

        cursor.execute(insert_query, data)
        connection.commit()

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
    finally:
        if 'connection' in locals():
            cursor.close()
            connection.close()

def check_phone(phone):
    cursor.execute("SELECT name FROM users WHERE phone = %s", (phone,))
    num=cursor.fetchone()
    try:
        main=num[0]
    except:
        return None
    # get_name(phone)
    return main
# print(check_phone())
def get_name(phone):
    cursor.execute("SELECT name FROM users WHERE phone = %s", (phone,))
    name=cursor.fetchone()
    try:
        main=name[0]
    except:
        return None
    return main

def already_exist(number):
    query = "SELECT * FROM users WHERE phone=%s"
    try:
        cursor.execute(query, (number,))
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        if results:
            row_dict = dict(zip(columns, results[0]))
            return True
        else:
            return False
    finally:
        cursor.close()
        connection.close()

def get_data(username,password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ved24072003",
        database="infotechacademyrewa"
    )
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    try:
        cursor.execute(query, (username, password))
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        if results:
            row_dict = dict(zip(columns, results[0]))
            return row_dict
        else:
            return False
    finally:
        cursor.close()
        connection.close()


def subject(language):

    query = "SELECT COUNT(*) FROM users WHERE language=%s"
    cursor.execute(query, (language,))
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return result 


def total_students():
    query="select count(*) from users"
    cursor.execute(query, ())
    result = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    return result
print(total_students())
# print(get_data(username='sauravpathak24072003@gmail.com',password='ved@2407'))
# data={"name":'Ved prakash pathak',"number":'+919752249543',"email":'ved24072003@gmail.com',"password":'ved@2407','course':'btech','language':'python'}
# save_data_to_mysql(data)