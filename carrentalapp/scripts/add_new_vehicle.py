import carrentalapp.aws_sql_credentials as awsdb

db = awsdb.db
cursor = db.cursor()

# Insert new vehicle into the database
while True:
    veh_id = input("Vehicle's ID: ")
    if len(veh_id) != 5:
        print("ID not in correct foramt. ID must be 5 characters, letters and numbers are allowed.\n************* ")
        continue
    else:
        break

while True:
    brand = input("Vehicle's brand: ")
    if len(brand) > 20:
        print("Brand name too long. Max 20 characters allowed.")
        continue
    else:
        break

while True:
    model = input("Vehicle's model: ")
    if len(model) > 20:
        print("Model name too long. Max 20 characters allowed.")
    else:
        break

while True:
    engine = input("Vehicle's engine: ")
    if len(engine) > 10:
        print("Engine size too long. Max 10 characters allowed.")
        continue
    else:
        break

while True:
    horse_power = input("Vehicle's horse power: ")
    if len(horse_power) > 5:
        print("Max 5 characters allowed.")
        continue
    else:
        break

price_per_day = input("Vehicle's price per day: ")

# Default value for how many times the specific vehicle was rented.
times_rented = 0  

#Enter a URL address for the specific vehicle from https://www.auto-data.net
full_specs_url = input("Enter vehicle's full specs page: ")

with db.cursor():
    sql = """INSERT INTO vehicles (vehichle_id, brand, model, engine_size, horse_power, price_per_day, times_rented, full_specs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (veh_id, brand, model, engine, horse_power, price_per_day, times_rented, full_specs_url))
    print("New vehicle {brand} {model} with ID {veh_id} successfully added.")
    db.commit()