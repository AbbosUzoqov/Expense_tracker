from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.database import get_db
from models.expense import Expense
from schemas.expense import ExpenseCreate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.get("/")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(Expense).all()
    return expenses

@router.get("/{expense_id}")
def get_expense_by_id(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.post("/", response_model=ExpenseResponse)
def create_expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense_data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense
@router.put("/expense_id}")
def put_expense(expense_id: int, expected_data: ExpenseCreate, db: Session = Depends(get_db)):
    put_expenses = db.query(Expense).filter(Expense.id == expense_id).first()
    if put_expenses is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    put_expenses.amount = expected_data.amount
    put_expenses.category = expected_data.category
    db.commit()
    db.refresh(put_expenses)
    return put_expenses