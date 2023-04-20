import mysql.connector

connectiondb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="00000",
    database="jornal",)
cursordb = connectiondb.cursor()

query = "INSERT INTO staff (surname, name, patronymic, job, phone, login, password, tip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
values = ('surname_value', 'name_value', 'patronymic_value', 'job_value', 'phone_value', 'root', '0000', 'polzovatel')
cursordb.execute(query, values)

connectiondb.commit()
connectiondb.close()