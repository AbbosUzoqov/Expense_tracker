from database.database import Base
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, func

class Expense(Base):
  __tablename__='Expenses'
  id: Mapped[int] = mapped_column(primary_key=True)
  title:Mapped[str] = mapped_column(nullable=False)
  amount:Mapped[float] = mapped_column(nullable=False)
  category:Mapped[str] = mapped_column(nullable=False)
  created_at:Mapped[datetime] = mapped_column(server_default=func.now())
