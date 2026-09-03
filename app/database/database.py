from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_DB = 'postgresql:///./postgres+tracker_api'

engine = create_engine(SQL_DB, connect_args={'check_same_thread': False})

session_local = sessionmaker(autoflush=False, autocommit=False, bind = engine)

base = declarative_base()

