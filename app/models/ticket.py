from sqlalchemy import Boolean, Column, Date, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import TimestampedModel
# from app.models.event import event_user_association


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))


    events = relationship("Event", back_populates="tickets")
    users = relationship("User", back_populates="tickets")
