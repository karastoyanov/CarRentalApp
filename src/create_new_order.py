# TO DO:
# order_id data type in MySQL to be change(longer VARCHAR with min. 10 symbols) !!!!!  DONE !!!!! 
# in orders table(in MySQL DB) new column to be added with deadline/order duration date !!!! DONE !!!!
# to do a order counter for the respective customer


import aws_sql_credentials as awsdb
import random
import datetime


db = awsdb.db
cursor = db.cursor()


# Function to create new order ID
def generate_id(lenght):
    order_id = []
    for i in range(lenght):
        if i == 0 or i == 1:
            order_id.append(chr(random.randrange(65, 90)))
        else:
            order_id.append(chr(random.randrange(48, 57)))
    result = ''.join(order_id)
    return result


# Fucntion to verify if the order is already exisitng
def check_for_doubles(order_id):
    cursor.execute("""SELECT * FROM orders""")
    result = cursor.fetchall()
    for row in result:
        to_check = row[0]
        if order_id == to_check:
            return True
        else:
            continue
    return False


while True:
    order_id = generate_id(10)
    if check_for_doubles(order_id) is False:
        break

# Default value for new orders
order_status = 'OPEN'

# Select the customer who open the orders
while True:
    f_name, l_name = [x for x in input("Insert customer's first and last name:\n").split()]
    # This one checks if the customer is already in the dabase
    sql = """SELECT * FROM customers WHERE first_name LIKE %s AND second_name LIKE %s"""
    result = cursor.execute(sql, (f_name,l_name))
    query_result = cursor.fetchall()
    if query_result:
        break
    else: 
        # In case that the customer doesn't exist in the database, 
        # the fuction for creating a new customer will be called
        print('*************************\nCustomer does not exist!\nA new record will be created\n')
        exec(open('add_customer.py').read())
        

# Select the desired vehicle
while True:
    cursor.execute("""SELECT * FROM vehicles""")
    result = cursor.fetchall()
    for row in result:
        print("************************************************************************************************")
        print("Vehicle ID: ", row[0])
        print("Vehicle Brand: ", row[1])
        print("Vehicle Model: ", row[2])
        print("Price Per Day: ", row[5] + " USD")
        print("************************************************************************************************")
        print('\n')
    user_choice = input("Select the vehicle ID:\n")
    sql = """SELECT * FROM vehicles WHERE vehicle_id = %s"""
    result = cursor.execute(sql, (user_choice))
    query_result = cursor.fetchone()
    if query_result:
        current_vehicle = query_result[1] + " " + query_result[2]
        print(f"Successfully selected {current_vehicle}")
        break
    else:
        print(f"Vehicle with {user_choice} does not exist. Please select a valid ID: \n")
        continue


# Save the current date as creating date for the order
current_date = datetime.datetime.now()
date = current_date.strftime("%x")

# How many days the order will be open
while True:
    duration = input("Please select the order duration in days: ")
    if duration.isdigit() is False or duration.isdigit() < 1 or duration.isdigit() > 30:
        print("Wrong format! Please select number between 1 and 30")
        continue
    else:
        break

# Total price calculation
total_price = int(duration) * int(row[5])
print("\n************************************************************************************************")
print(f"Order ID: {order_id}")
print(f"Customer: {f_name} {l_name}")
print(f"Vehicle: {current_vehicle}")
end_date = current_date + datetime.timedelta(days=int(duration))
print(f"Order valid until: {end_date}")
print(f"Final price: \n{total_price} USD")
print("\n************************************************************************************************")


# Save or discard order creating
while True:
    to_save = input("\nDo you want to save and create this order?(Y/N)?\n")
    if to_save == "Y":
        with db.cursor():
            sql_query = "INSERT INTO orders (order_id, order_status, cust_first_name, cust_last_name, vehicle, \
                order_creation_date, duration_in_days, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql_query, (order_id, order_status, f_name, l_name, current_vehicle, current_date, duration, total_price))
            print("\nNew order was successfully created!")
            db.commit()
            break
    else:
        print("\nProgram stoped without creating a new order.")
        break
    
    
