from datetime import datetime

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update

from sqlalchemy.orm import Session

from models.transaction_category import TransactionCategory, TransactionCategoryModel

def get_all_categories(engine):
    session = Session(engine)
    statement = select(TransactionCategory).where(TransactionCategory.logical_delete == False)
    result = session.execute(statement)
    categories = []
    for row in result:
        categories.append(TransactionCategoryModel(
            id=row[0].id,
            name=row[0].name,
        ))
    
    session.close()
    return categories