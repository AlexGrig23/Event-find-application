from typing import Optional

from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserUpdate, UserSignUp
from app.utils import verify_password

from .base import CRUDBase


class UserCRUD(CRUDBase[User, UserSignUp, UserUpdate]):
    def get_user_by_email(self, db: Session, email: EmailStr) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user


user_crud = CRUDBase(UserCRUD)