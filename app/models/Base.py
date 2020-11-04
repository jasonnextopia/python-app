from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

db_host = getenv('DBHOST')
db_user = getenv('DBUSER')
db_password = getenv('DBPASSWORD')

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}")

Base = declarative_base()