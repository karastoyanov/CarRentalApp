import aws_sql_credentials as awsdb

db = awsdb.db

id = int(input())
fname = input()
sname = input()
    
cursor = db.cursor()

with db:
    with db.cursor():
        sql = 'use carrentaldb'
        cursor.execute(sql)
    
    with db.cursor():
        sql2 = 'select * from customers'
        cursor.execute(sql2)
        result = cursor.fetchall()
        print(result)
    
    with db.cursor():
        sql3 = """INSERT INTO customers VALUES (id, 'fname', 'sname')"""
        # record = (id, fname, sname)
        cursor.execute(sql3)
    
    db.commit()



gfjfghsdfjghdfghdfhjkg