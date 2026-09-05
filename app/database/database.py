from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



SQL_DB = 'postgresql://postgres:boss05@localhost:5432/tracker_api'

engine = create_engine(SQL_DB, echo=True)

session_local = sessionmaker(autoflush=False, autocommit=False, bind = engine)

Base = declarative_base()

