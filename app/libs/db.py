from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app.libs.Config import Config
from app.libs.singleton import Singleton

Base = declarative_base()

class DBEngine(metaclass=Singleton):
    _engine = None

    def __init__(self, database_uri):
        if self._engine is None:
            self._engine = create_engine(database_uri, pool_size=60, poolclass=QueuePool)

    def get_db_engine(self):
        return self._engine

def get_conn_str():
    return f"mysql+pymysql://{Config.DBUSER}:{Config.DBPASSWORD}@{Config.DBHOST}/{Config.DBNAME}"

def get_db_engine(conn_str=None):
    if conn_str is None:
        conn_str = get_conn_str()

    return DBEngine(conn_str).get_db_engine()

def get_session(engine):
    return sessionmaker(bind=engine)()