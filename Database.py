import mysql.connector as ms
db = ms.connect(user = "root", host = "localhost", password = "sql#@$678*&*&//", database = "bankmanagment")
db_ = db.cursor()
#Database Bankmanagment including all customers!
def query(str):
    db_.execute(str)
    result = db_.fetchall()
    return result 
class customer(): #class to add the customers in the database
    def __init__(self, username, password, name, age, city, account_number):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.account_number = account_number
    def insert_details(self): #method to insert details of customer in the customer's table
        query(f"INSERT INTO customers (username, password, name, age, city, account_number, balance, status) VALUES ('{self.username}', '{self.password}', '{self.name}', {self.age}, '{self.city}', '{self.account_number}', 0, 1);")
        db.commit()
        print("Details entered successfully!", "Account created!")
