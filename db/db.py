endpoint="venkatdb.co32keuo8nsj.us-east-1.rds.amazonaws.com"
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

from psycopg2.extras import RealDictCursor

username,pwd='postgres','Venkat182611'
dbname='postgres'

# DBconnect=f"postgressql://{username}:{pwd}@{endpoint}:5432/{dbname}"

# engine=create_engine(DBconnect)


try:
    conn=psycopg2.connect(host=endpoint,database=dbname,user=username,password=pwd,cursor_factory=RealDictCursor)
    cursor=conn.cursor()
    print("success")
except Exception as e:
    print(e)