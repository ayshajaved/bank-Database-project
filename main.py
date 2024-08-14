import mysql.connector as ms                           #connecting python to the mysql database
from Database import *                                 #importing user defined module
from customers_tables import *                         #importing user defined module
import random                                          #importing random to generate bank account for the customers
   
def Signup():   
    while True:                                       #method for signing up
        username = input("Enter username:-")
        x = query(f"select username from customers where username = '{username}';")
        if x:
            print("User name is not present!Try again!")
        else:
            print("User name available! Procced further.")
            while True:
                password = input("Enter Pin(4 digits):- ")
                if len(password) ==4:
                    name = input("Enter name:- ")
                    age = int(input("Enter age:- "))
                    city = input("Enter city:- ")
                    account = random.randrange(10000000, 100000000)
                    while True:
                        if query(f"select account_number from customers where account_number = '{account}';"):
                            continue
                        else:
                            print(f"Your account number is {account}! With balance 0 and status 1!")
                            break
                    customer_obj = customer(username, password, name, age, city, account)
                    customer_obj.insert_details()
                    break
                else:
                    print("Pin is invalid!Try again.")
            break
            
def Signin():                                          #method for signing in
    while True:   
        username = input("Enter username:-")
        
        x = query(f"select username from customers where username = '{username}';")
        if x:
            print("Correct Username!")
            while True:
                password = input("Enter password:- ")
                result =query(f"select password from customers where username ='{username}';")
                if result[0][0] == password:
                    print(f"Welcome {username.capitalize()}!")
                    bank_facilities(username=username, password=password)
                    break      
                else:
                    print("Password is incorrect!Try again")
            break
        else:
            print("Username is Wrong! Enter valid username!")
            

def bank_facilities(username , password):               #method for facilities for a particular customer
    acc = query(f"select account_number from customers where password = '{password}';")
    account = acc[0][0]
    obj = Customer_table(username,account)  
    print("Welcome to Bank facilities!")
    
    while True:
        try:                                         #bank facilities
            choice = int(input('''Enter your choice:-
                        1) Balance enquiry
                        2) Deposit Money
                        3) Withdraw Money
                        4) Fund Transfer
                        5) Exit
                        '''))
            if choice == 1:
                obj.balanceenquiry()
            elif choice ==2:
                while True:
                    amount = int(input("Enter amount to be deposited:- "))
                    if amount >0:
                        print(f"{amount} rupee has been deposited!")
                        obj.deposit(amount)
                        obj.transactions(amount, "Money deposited!")#updating particular customer's transaction record
                        break
                    else:
                        print("Enter Valid amount!")
            elif choice ==3:
                while True:
                    amount = int(input("Enter amount to be Withdrawn:- "))
                    if amount >0:
                        obj.withdraw(amount)
                        break
                    else:
                        print("Enter Valid amount!")
            elif choice ==4:
                while True:
                    receiver = int(input("Enter the bank account whom you wanna transfer:-"))
                    if query(f"select account_number from customers where account_number = '{receiver}';"):
                        while True:
                            money = int(input("Enter amount to be transfered!:-"))
                            x = query(f"Select balance from customers where username = '{username}';")
                            if x[0][0] >= money:
                                remark = input("Enter remarks:-")
                                obj.fund_transfer(receiver, money)
                                obj.transactions(money, remark)             #updating particular customer's transaction record
                                break                   
                            else:
                                print("Amount entered is more than your balance!")
                        break
                    else:
                        print("Enter Valid Receiver Bank Account!")
            elif choice == 5:
                exit()
            else:
                print("Enter valid choice!!")
        except Exception as er:
            print(f"ERROR:{er}")
def main():
    print("****************************")
    print("WELCOME TO THE BANK OF PYTHON")
    print("****************************")
    while True:
        try:
            choice = int(input('''Enter your choice:- 
                                1) Sign up(NEW CUSTOMER)
                                2) Sign In(PRESENT CUSTOMER)
                                3) Exit
                                '''))
            if choice == 1:
                Signup() 
            elif choice == 2:
                Signin()
            elif choice == 3:
                exit()
            else:
                print("Invalid choice!")
        except Exception as er:
            print(f"ERROR:{er}")
if __name__ == "__main__":                              #checking the file name and running main function
    main()   



