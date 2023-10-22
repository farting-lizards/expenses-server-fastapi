from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class AccountBase(BaseModel):
    id: int
    name: str


class Account(AccountBase):
    pass


class ExpenseBase(BaseModel):
    amount: float
    currency: str
    timestamp: str = Field(examples=["2023-10-22 14:30:34"])
    category: str
    description: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "amount": 190,
                    "currency": "CHF",
                    "timestamp": "2023-10-22 14:30:34",
                    "category": "Grocery",
                    "description": "E. Leclerc",
                    "account_id": 1,
                }
            ]
        }
    }

    @field_validator("timestamp")
    @classmethod
    def validate_timestamp(cls, value: str) -> datetime:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


class ExpenseCreate(ExpenseBase):
    account_id: int


class Expense(ExpenseBase):
    id: int
    account: Account

    class Config:
        from_attributes = True
