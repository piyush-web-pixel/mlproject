import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv

# import psycopg
import psycopg2

load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
passs=os.getenv('password')
db=os.getenv('db')
port=os.getenv('port')


 

def read_sql_data():
    logging.info('reading sql database started')
    try:
        mydb= psycopg2.connect(
            host='localhost',
            user='postgres',
            password=1234,
            database='mldatabase',
            port=5432
        )

        logging.info('connection established')

        query = "SELECT * FROM student"

        df = pd.read_sql_query(query, mydb)
        print(df.head())
        # mydb.close()

        return df
    
    except Exception as e:
        raise CustomException(e,sys)