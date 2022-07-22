import mysql.connector
import pymysql

db = pymysql.connect(host = "carrental-db2.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com", user = "admin", password = "Password1", port = 3306)

# cursor = db.cursor()
# cursor.execute('select version();')

# data = cursor.fetchone()

# with db:
#     with db.cursor() as cursor:
#         sql = 'use carrentaldb'
#         cursor.execute(sql)
    

#     with db.cursor() as cursor:
#         sql2 = 'insert into customers values (001, "Ivan", "Ivanov")'
#         cursor.execute(sql2)
#         result = cursor.fetchall()
    
#     with db.cursor() as cursor:
#         sql3 = 'select * from customers'
#         cursor.execute(sql3)
#         result = cursor.fetchall()
#         print(result)
#     db.commit()