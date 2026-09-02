from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
  name: str
  surname: str
  age: int
  email: EmailStr
  password: str

class UserOut(BaseModel):
  id: int
  name: str
  surname: str
  age: int
  email: EmailStr

  class Config:
    from_attributes = True

class CategoryCreate(BaseModel):
  name: str

class CategoryOut(BaseModel):
  id: int
  name: str
  user_id: int

  class Config:
    from_attributes = True

class ExpenseCreate(BaseModel):
  amount: int
  description: str
  date_time: date
  category_id: int

class ExpenseOut(BaseModel):
  id: int
  amount: int
  description: str
  date_time: date
  category_id: int
  user_id: int
  created_at: date

  class Config:
    from_attributes = True
