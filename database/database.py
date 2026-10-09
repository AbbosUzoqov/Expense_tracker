import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQL_DB = os.getenv("DATABASE_URL")
if SQL_DB is None:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(SQL_DB, echo=False)

session_local = sessionmaker(autoflush=False, autocommit=False, bind = engine)

Base = declarative_base()

def get_db():
  db = session_local()
  try:
    yield db
  finally:
    db.close()
  


