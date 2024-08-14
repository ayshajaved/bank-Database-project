'''
Python is connected to the database MYSQL through mysql.connector
'''
import mysql.connector as ms
db = ms.connect(user = "root", host = 'localhost', password= 'sql#@$678*&*&//')
if db.is_connected():
    print("Database is connected!") 

 