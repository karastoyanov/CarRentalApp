#Function to show all orders

import aws_sql_credentials as awsdb

db = awsdb.db
cursor = db.cursor()
cursor.execute("SELECT * FROM orders")
result = cursor.fetchall()

for row in result:
    
    print("*************************************************************")
    print("Order ID:", row[0])
    print("Order Status:", row[1])
    print("Name:", row[2] + " " + row[3])
    print("Vehicle:", row[4])
    print("Date of order:", row[5])
    print("Days duration:",row[6])
    print("Total price:", row[7])
    print("*************************************************************")

print("Total orders:", len(result))