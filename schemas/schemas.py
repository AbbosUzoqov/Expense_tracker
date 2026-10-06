from datetime import date
from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
  name: str
  surname: str
  age: int
  email: EmailStr
  password: str

class UserOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  name: str
  surname: str
  age: int
  email: EmailStr


class CategoryCreate(BaseModel):
  name: str

class CategoryOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  name: str
  user_id: int

class ExpenseCreate(BaseModel):
  amount: int
  description: str
  date_time: date
  category_id: int

class ExpenseOut(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  amount: int
  title: str
  date_time: date
  category_id: int
  user_id: int
  created_at: date
