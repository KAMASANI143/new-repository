import psycopg2
from config import DATABASE, USER, PASSWORD, HOST, PORT
import string
import json 
def conn_db():
    conn = psycopg2.connect(database = DATABASE, user = USER, password =PASSWORD, host = HOST, port = PORT)
    if conn:
        cur = conn.cursor()
        print('connection done')
        return conn,cur

    else:
        print('not connected')
    

