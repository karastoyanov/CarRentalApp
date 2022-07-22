import mysql.connector
import sys
import boto3
import os

ENDPOINT = 'carrental-db.cvwquqtl5fz5.eu-central-1.rds.amazonaws.com'
PORT = '3306'
USER = 'Karastoyanov'
REGION = 'eu-central-1c'
DBNAME = 'carrental-db'

os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

session = boto3.Session(profile_name='Karastoyanov')
client = session.cleint('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd=token, port=PORT, database=DBNAME, ssl_ca='rds-ca-2019')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))