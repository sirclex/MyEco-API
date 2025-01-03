from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.transaction import TransactionCreate, TransactionUpdate, TransactionResponse
from schemas.debt import DebtCreate
from schemas.message import Message
from logic import transaction_logic
from api.deps import get_db

router = APIRouter()

@router.get("", response_model=List[TransactionResponse])
def get_all_transactions(db: Session = Depends(get_db)) -> Any:
    return transaction_logic.get_all_transactions_info(db)

@router.post("", response_model=TransactionResponse)
def create_transaction(*, db: Session = Depends(get_db), transaction_in: TransactionCreate, debts_in: list[DebtCreate]) -> Any:
    return transaction_logic.create_transaction(db, transaction_in, debts_in)

@router.put("", response_model=TransactionResponse)
def update_transaction(*, db: Session = Depends(get_db), transaction_in: TransactionUpdate) -> Any:
    return transaction_logic.update_transaction(db, transaction_in)

@router.delete("", response_model=Message)
def delete_transaction(*, db: Session = Depends(get_db), id: int) -> Any:
    return transaction_logic.delete_transaction(db, id)