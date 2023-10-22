from sqlalchemy import (
    DECIMAL,
    TIMESTAMP,
    VARCHAR,
    Column,
    ForeignKey,
    Integer,
    Sequence,
)
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from expenses_app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, Sequence("expense_sequence"), primary_key=True, index=True)
    amount = Column(DECIMAL, nullable=False)
    currency = Column(VARCHAR(10), nullable=False, default="EUR")
    timestamp = Column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=current_timestamp,
        onupdate=current_timestamp,
    )
    category = Column(VARCHAR(45), nullable=False)
    description = Column(VARCHAR(200), default=None)
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship(
        "Account", back_populates="expenses", foreign_keys="account_id"
    )


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, Sequence("hibernate_sequence"), primary_key=True, index=True)
    name = Column(VARCHAR(100), nullable=False)

    expenses = relationship("Expense", back_populates="account")
