from typing import Literal
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy import desc, asc
from sqlalchemy.orm import Session
from database.database import get_db
from models.expense import Expense, Summary
from schemas.expense import ExpenseCreate, ExpenseResponse

router = APIRouter(prefix="/expenses", tags=["Expenses"])

ALLOWED_SORT_FIELDS = {
    "created_at": Expense.created_at,
    "amount": Expense.amount,
    "category": Expense.category,
}


def get_expense_or_404(expense_id: int, db: Session) -> Expense:
    expense = db.get(Expense, expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@router.get("/", response_model=list[ExpenseResponse])
def get_expenses(
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    category: str | None = None,
    sort_by: Literal["created_at", "amount", "category"] = "created_at",
    order: Literal["asc", "desc"] = "desc",
):
    query = db.query(Expense)
    if category:
        query = query.filter(Expense.category == category)

    direction = asc if order == "asc" else desc
    query = query.order_by(direction(ALLOWED_SORT_FIELDS[sort_by]), direction(Expense.id))
    return query.offset(skip).limit(limit).all()


@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense_by_id(expense_id: int, db: Session = Depends(get_db)):
    return get_expense_or_404(expense_id, db)


@router.post("/", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED)
def create_expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense_data.model_dump())
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.put("/{expense_id}", response_model=ExpenseResponse)
def update_expense(expense_id: int, data: ExpenseCreate, db: Session = Depends(get_db)):
    expense = get_expense_or_404(expense_id, db)
    for field, value in data.model_dump().items():
        setattr(expense, field, value)
    db.commit()
    db.refresh(expense)
    return expense


@router.delete("/{expense_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = get_expense_or_404(expense_id, db)
    db.delete(expense)
    db.commit()
