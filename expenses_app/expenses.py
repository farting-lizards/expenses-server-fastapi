from sqlalchemy.orm import Session
from .api_models import Expense, ExpenseCreate
from . import database_models


def create_expense(
    db: Session, expense_to_create: ExpenseCreate
) -> database_models.Expense:
    expense = database_models.Expense(
        amount=expense_to_create.amount,
        currency=expense_to_create.currency,
        category=expense_to_create.category,
        description=expense_to_create.description,
        account_id=expense_to_create.account_id,
    )
    print(expense_to_create)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


def get_expense(db: Session, id: int):
    return db.query(database_models.Expense).get(id)


def get_expenses(db: Session):
    return db.query(database_models.Expense).all()
