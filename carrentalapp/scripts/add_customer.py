# TO DO: 
# New field with numbers of orders/car rentals

import carrentalapp.aws_sql_credentials as awsdb
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtCore import (QDateTime, QDate, QTime, Qt)
import datetime
import random
from carrentalapp import addCustomer

db = awsdb.db
cursor = db.cursor()

# Function to verify if the new customer's ID is already exisitng in the database(Not allowed two records with same ID)
def check_for_doubles(customer_id):
    cursor.execute("""SELECT * FROM customers""")
    result = cursor.fetchall()
    for row in result:
        to_check = row[0]
        if customer_id == to_check:
            return True
        else:
            continue
    return False
    
# Function to create a new random customer ID -- > \
    # Frist two chars are capital letters followed by 8 digits  
def generate_id(lenght):
    customer_id= []
    for i in range(lenght):
        if i == 0 or i == 1:
            customer_id.append(chr(random.randrange(65, 90)))
        else:
            customer_id.append(chr(random.randrange(48, 57)))
    result = ''.join(customer_id)
    return result

# Function to verify if another customer with same ID already exists
def check_for_doubles(customer_id):
    cursor.execute("""SELECT * FROM customers""")
    result = cursor.fetchall()
    for row in result:
        to_check = row[0]
        if customer_id == to_check:
            return True
        else:
            continue
    return False

while True:
    customer_id = generate_id(10)
    if check_for_doubles(customer_id) is False:
        break


while True:   
    first_name = input("Customer's first name: ")
    if len(first_name) > 50:
        print("First name too long! Max 50 symbols allowed.\n*************")
        continue
    else:
        break
    
while True:
    second_name = input("Customers's last name: ")
    if len(second_name) > 50:
        print("Last name too long! Max 50 symbols max allowed.\n*************")
        continue
    else:
        break
    
while True:   
    phone_number = input("Enter customer's phone number in format XXXX/XXXXXX: ")
    if len(phone_number) > 15:
        print("Phone number format incorect. 15 symbols max allowed.\n*************")
        continue
    else:
        break

email = input("Enter customer's email address: ")
cust_status = 'NEW'

#Just a try with the date not finished its not the way i would like but give it a try it works also added a column in the table 
date = datetime.datetime.now();
# date = customerDate.strftime("%x")





with db.cursor():
    # This one below works
    sql = """INSERT INTO `customers` (cust_id, first_name, second_name, phone, email, cust_status, date) VALUES (%s, %s, %s, %s, %s, %s, %s) """
    cursor.execute(sql, (customer_id, first_name, second_name, phone_number, email, cust_status, date))
    print("New customer {first_name} {second_name} with ID {cust_id} successfully added.")
    db.commit()










