from fastapi import FastAPI, status, HTTPException, APIRouter, Depends, Body
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing_extensions import Any

from app import schemas
from app.dependencies.database import get_db
from app.utils import get_hashed_password, create_access_token, create_refresh_token

from app.services.user import user_crud


router = APIRouter()


@router.post("/sign-up", response_model=schemas.UserSignUpResponse, status_code=201)
def register_user(user_data: schemas.UserSignUp, db: Session = Depends(get_db)) -> Any:
    """
    Register a new user.
    """
    existing_user = user_crud.get_user_by_email(db, email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists",
        )

    hashed_password = get_hashed_password(user_data.password)
    user_data.password = hashed_password
    user = user_crud.create(db, obj_in=user_data)
    response = schemas.UserSignUpResponse(
        **user.__dict__,
        access_token=create_access_token({"user_id": user.id}),
        refresh_token=create_refresh_token({"user_id": user.id}),
    )

    return response


@router.post("/login", response_model=schemas.Token)
def login(db: Session = Depends(get_db), user_data: schemas.UserLogin = Body(...)) -> Any:
    """
    Endpoint to allow users to login

    :param db: DB session
    :param user_data: Body object with email and password
    :return: jwt access and refresh token
    """
    user = user_crud.authenticate(db, email=user_data.email, password=user_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return {
        "access_token": create_access_token({"user_id": user.id}),
        "refresh_token": create_refresh_token({"user_id": user.id}),
    }
