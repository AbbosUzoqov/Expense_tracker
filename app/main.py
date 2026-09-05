from database.database import Base, engine
from fastapi import FastAPI
import models

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def root_get():
  return {"status": "Database tables created or already exist"}