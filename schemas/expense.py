from fastapi import FastAPI
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field, ConfigDict

class ExpenseCreate(BaseModel):
  title: str = Field(min_length=1, max_length=200)
  amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
  category: str = Field(min_length=1, max_length=300)

class ExpenseResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  title: str
  amount: Decimal
  category: str 
  created_at: datetime

class CategoryTotal(BaseModel):
  category: str
  total: Decimal

class ExpenseSummary(BaseModel):
  total: Decimal
  by_category: list[CategoryTotal]

