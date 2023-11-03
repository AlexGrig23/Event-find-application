from typing import Generator

from app.db.session import SessionLocal

from datetime import datetime


from fastapi import Depends, HTTPException

from pydantic import ValidationError
from sqlalchemy.orm import Session
from starlette import status



def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
