from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .expense import Expense
import models
from database.database import get_db
from .expenses import ExpenseCreate


router = APIRouter(prefix='/expenses', tags = ["Expenses"])

router.post("/")
def expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
  new_expense = Expense(**expense_data.model_dump())
  db.add(new_expense)
  db.commit()
  db.refresh(new_expense)
  return new_expense
