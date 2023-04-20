import mysql.connector

# Подключаемся к базе данных
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="00000",
    database="jornal"
)

# Создаем курсор для выполнения запросов
cursor = connection.cursor()

# Выполняем запрос на вывод всех данных из таблицы staff
cursor.execute("SELECT * FROM staff")

# Получаем все строки из результата запроса
rows = cursor.fetchall()

# Выводим результат
for row in rows:
    print(row)

# Закрываем курсор и соединение с базой данных
cursor.close()
connection.close()