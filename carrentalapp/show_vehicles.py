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
        print("Vehicle Engine Size: ", row[3] +"cm3")
        print("Vehicle Horse power: ", row[4] + "HPs")
        print("Price Per Day: ", row[5] + " USD")
        print("Times rented: ", row[6])
        print("Vehicle Full Specs at: ", row[7])
        print("************************************************************************************************")
        print('\n')
print("\n!!!!!!!!END!!!!!!!!")
print(f'Total records: {len(result)}')