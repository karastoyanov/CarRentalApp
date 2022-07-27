# Function to list all existing vehicles
import aws_sql_credentials as awsdb

db = awsdb.db
cursor = db.cursor()
cursor.execute("SELECT * FROM vehicles")
result = cursor.fetchall()

for row in result:
    for row in result:
        print("************************************************************************************************")
        print("Vehicle ID: ", row[0])
        print("Vehicle Brand: ", row[1])
        print("Vehicle Model: ", row[2])
        print("Vehicle Engine Size: ", row[3])
        print("Vehicle Horse power: ", row[4])
        print("Price Per Day(USD): ", row[5])
        print("************************************************************************************************")
        print('\n')
print("\n!!!!!!!!END!!!!!!!!")
print(f'Total records: {len(result)}')