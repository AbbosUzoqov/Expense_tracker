from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import os


SQL_DB = os.getenv("DATABASE_URL",'postgresql://postgres:boss05@localhost:5432/tracker_api')

engine = create_engine(SQL_DB, echo=False)

session_local = sessionmaker(autoflush=False, autocommit=False, bind = engine)

Base = declarative_base()

def get_db():
  db = session_local()
  try:
    yield db
  finally:
    db.close()
  


