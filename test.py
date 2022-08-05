import aws_sql_credentials as awsdb
import random
import datetime


db = awsdb.db
cursor = db.cursor()


cursor.execute("SELECT * FROM vehicles")
row = cursor.fetchall()

for result in row:
    print("************************************************************************************************")
    print("Vehicle ID: ", result[0])
    print("Vehicle Brand: ", result[1])
    print("Vehicle Model: ", result[2])
    print("Price Per Day: ", result[5] + " USD")
    print("************************************************************************************************")
    print('\n')

cus_input = input("Insert: ")

for result in row:
        
    if cus_input == result[0]:
        print(f"You have chosen {result[1]} {result[2]} great choice!" )

