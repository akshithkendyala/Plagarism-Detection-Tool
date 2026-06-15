import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Pavan@5ed",
    database="plagiarism_db"
)

cursor = connection.cursor()