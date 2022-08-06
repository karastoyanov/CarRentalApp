# TO DO: 
# New field with numbers of orders/car rentals


# Function to add new customer into the database;

import aws_sql_credentials as awsdb
import datetime 

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
    

# Insert new customer into 'customers' table
while True:
    cust_id = input("Customers's ID(in format XXXXX):")
    if check_for_doubles(cust_id) is True:
        print("\nCustomer's ID already existing")
        continue
    
    if len(cust_id) != 5:
        print('ID not in correct format. ID must be 5 characters, letters and numbers are allowed.\n*************')
        continue
    else:
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
    cursor.execute(sql, (cust_id, first_name, second_name, phone_number, email, cust_status, date))
    print("New customer {first_name} {second_name} with ID {cust_id} successfully added.")
    db.commit()









