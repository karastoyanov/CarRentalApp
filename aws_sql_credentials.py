import pymysql

# AWS RDS connector / DO NOT CHANGE BELOW'S DATA
db = pymysql.connect(host = "carrentalapp-db.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com", 
                     user = "admin", 
                     password = "Password1", 
                     port = 3306)
cursor = db.cursor()
cursor.execute("""USE carrental""")
db.commit()
