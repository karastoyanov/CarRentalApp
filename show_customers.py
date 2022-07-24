# Function to list all existing customers
import aws_sql_credentials as awsdb

db = awsdb.db
cursor = db.cursor()
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()
for row in result:
    print("************************************************************************************************")
    print("Customer ID: ", row[0])
    print("Customer Name: ", row[1] + " " + row [2])
    print("Customer Phone number: ", row[3])
    print("Customer Email address: ", row[4])
    print("Customer Status: ", row[5])
    print("************************************************************************************************")
    print('\n')
print("\n!!!!!!!!END!!!!!!!!")
print(f'Total records: {len(result)}')