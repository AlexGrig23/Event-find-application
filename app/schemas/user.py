from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.models.user import UserTypeEnum


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr
    is_active: bool
    role: UserTypeEnum
    date_of_birth: date



class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserSignUp(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    password: str
    date_of_birth: date
    role: UserTypeEnum

    class Config:
        from_attributes = True


# class UserCreate(BaseModel):
#     first_name: str
#     last_name: str
#     email: EmailStr
#     password: str
#     user_type: str
#     date_of_birth: date


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    date_of_birth: Optional[date] = None


class UserSignUpResponse(BaseModel):
    access_token: str
    refresh_token: str





    #
    # password = Column(String, nullable=False)
    # is_active = Column(Boolean(), default=True)
    # role = user_type = Column(Enum(UserTypeEnum), nullable=False)
    # date_of_birth = Column(Date(), nullable=False)
    #
    # events = relationship("Event", back_populates="users") # secondary=event_user_association,
    # tickets = relationship("Ticket", back_populates="users")