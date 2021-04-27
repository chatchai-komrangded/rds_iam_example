
import mysql.connector
import sys
import boto3
import os

ENDPOINT="RDS ENDPOINT"
PORT="3307"
USR="iamuser"
REGION="ap-southeast-1"
DBNAME="devmysql"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = boto3.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME)
    cur = conn.cursor()
    cur.execute("""SELECT * from t""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))          
                