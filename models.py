from datetime import date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
  pass
class User(Base):
  __tablename__ = "user"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  surname: Mapped[str]
  age: Mapped[int]
  email: Mapped[str]
  hashed_password: Mapped[str]

class Category(Base):
  __tablename__='category'
  id: Mapped[int] = mapped_column(primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
  name: Mapped[str]

class Expenses(Base):
  __tablename__='expenses'
  id: Mapped[int] = mapped_column(primary_key=True)
  amount: Mapped[int]
  description: Mapped[str]
  date_time: Mapped[date]
  category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
  user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
  created_at: Mapped[date]