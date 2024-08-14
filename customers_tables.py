from Database import *                          #importing user defined module
import datetime                                 #Datetime for the transaction history managing.

class Customer_table():                         #class for the individual customer table creation.
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number= account_number
        self.table()
    
    def table(self):                            #method for table creation
        query(f"Create table if not exists {self.__username}_transactions( username varchar(20), account_number int,amount int,  datetime varchar(30), remarks varchar(30));")
    
    def transactions(self,am, string):          #Inserting the transaction record in the particular customer's table
        query(f"insert into {self.__username}_transactions (username, account_number, amount, datetime, remarks) values ('{self.__username}', {self.__account_number}, {am} , '{datetime.datetime.now()}', '{string}');")
        db.commit()
        print("Transaction added successfully!")
    
    def balanceenquiry(self):                   #method to show balance
        bal = query(f"select balance from customers where username = '{self.__username}';")
        print(f"Your balance is {bal[0][0]}")
    
    def deposit(self, amount):                  #method to deposit money and updating in the customer's table
        balance = query(f"select balance from customers where username = '{self.__username}';")
        new_balance = balance[0][0] + amount
        query(f"update customers set balance = {new_balance} where username = '{self.__username}';")
        db.commit()
        print("Your balance has been updated!")
        self.balanceenquiry()

    def withdraw(self, withdraw_amount):        #method to withdraw amount and updating the money in the customer's table
        balance = query(f"select balance from customers where username = '{self.__username}';")
        if balance[0][0] >= withdraw_amount:
            new_balance = balance[0][0] - withdraw_amount
            query(f"update customers set balance = {new_balance} where username = '{self.__username}';")
            db.commit()
            print("Your balance has been updated!")
            print(f"{withdraw_amount} rupee has been withdrawn!")
            self.balanceenquiry()
            self.transactions(withdraw_amount, "Money withdrawn!")#updating particular customer's transaction record
        else:
            print("Requested amount is more than the balance!")
            
    def fund_transfer(self, receiver, money):    #method to transfer fund
        balance = query(f"select balance from customers where account_number = '{receiver}';")
        new_balance = balance[0][0] + money
        query(f"update customers set balance = {new_balance} where account_number = '{receiver}';")
        db.commit()
        print(f"The amount of {money} has been transfered to the account {receiver} by {self.__username}!")
        user_name = query(f"select username from customers where account_number = {receiver};")
        user = user_name[0][0]
        st = f"Received from {self.__username}"
        query(f"insert into {user}_transactions (username, account_number, amount, datetime, remarks) values ('{user}', {receiver}, {money} , '{datetime.datetime.now()}', '{st}');")
        db.commit()
        b = query(f"select balance from customers where username = '{self.__username}';")
        ba = b[0][0]
        new = ba - money
        query(f"update customers set balance = {new} where username = '{self.__username}';")
        self.balanceenquiry()
    
    