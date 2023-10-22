from pydantic import BaseModel
from datetime import datetime


class ExpenseBase(BaseModel):
    id: int
    amount: float
    currency: str
    timestamp: datetime
    category: str
    description: str | None = None


class ExpenseCreate(ExpenseBase):
    account_id: int


class Expense(ExpenseBase):
    accounts: "Account"

    class Config:
        orm_mode = True


class AccountBase(BaseModel):
    id: int
    name: str


class Account(AccountBase):
    pass
