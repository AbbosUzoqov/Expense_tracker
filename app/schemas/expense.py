from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
  amount: float
  category: str

class ExpenseResponse(BaseModel):
  id: int
  amount: float = Field(gt=0)
  category: str | None = Field(default=None, max_length=300)
  created_at: datetime

  class Config:
    from_attributes = True
