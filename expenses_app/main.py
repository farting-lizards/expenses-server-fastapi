from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from expenses_app.database import SessionLocal, engine

from . import database_models, expenses
from .api_models import Expense, ExpenseCreate

database_models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Returning Expenses"}


@app.post("/expense/", response_model=Expense)
async def create(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return expenses.create_expense(db, expense)
