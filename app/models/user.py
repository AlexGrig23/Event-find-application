
import enum
from sqlalchemy import Boolean, Column, Date, Enum, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import TimestampedModel

# from app.models.event import event_user_association


class UserTypeEnum(enum.Enum):
    client = "user"
    admin = "admin"
    superadmin = "superadmin"


class User(TimestampedModel, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    role = Column(Enum(UserTypeEnum), nullable=False)
    date_of_birth = Column(Date(), nullable=False)

    events = relationship("Event", back_populates="users", lazy="dynamic") # secondary=event_user_association,
    tickets = relationship("Ticket", back_populates="users")

    # @property
    # def is_superuser(self) -> bool:
    #     return self.user_type == UserTypeEnum.superadmin



