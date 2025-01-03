from typing import Any

from fastapi import HTTPException, status

from schemas.identity_type import IdentityTypeCreate, IdentityTypeUpdate
import crud
from sqlalchemy.orm import Session
from constants import exceptions

def get_all_identity_types(db: Session) -> Any:
    identity_types = crud.identity_type.get_multi(db)
    return identity_types

def get_identity_type(db: Session, identity_type_id: int) -> Any:
    identity_type = crud.identity_type.get(db, identity_type_id)
    if not identity_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exceptions.IDENTITY_TYPE_NOT_FOUND
        )
    return identity_type

def create_identity_type(db: Session, identity_type_in: IdentityTypeCreate) -> Any:
    identity_type = crud.identity_type.create(db, obj_in=identity_type_in)
    return identity_type

def update_identity_type(db: Session, identity_type_in: IdentityTypeUpdate) -> Any:
    identity_type = crud.identity_type.get(db, identity_type_in.id)
    if not identity_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exceptions.IDENTITY_TYPE_NOT_FOUND
        )
    identity_type = crud.identity_type.update(db, db_obj=identity_type, obj_in=identity_type_in)
    return identity_type

def delete_identity_type(db: Session, identity_type_id: int) -> Any:
    identity_type = crud.identity_type.get(db, identity_type_id)
    if not identity_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exceptions.IDENTITY_TYPE_NOT_FOUND
        )
    crud.identity_type.delete(db, model_id=identity_type.id)
    return {"message": f"Identity type with ID = {id} deleted."}