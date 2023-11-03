from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.base import TimestampedModel


# event_user_association = Table(
#     "events",
#     Base.metadata,
#     Column("event_id", Integer, ForeignKey("event.id")),
#     Column("user_id", Integer, ForeignKey("user.id")),
# )
#
# #
# class Doctor(TimestampedModel, Base):
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     first_name = Column(String, nullable=False)
#     middle_name = Column(String, nullable=True)
#     last_name = Column(String, nullable=False)
#     experience = Column(Integer, nullable=False)
#     description = Column(Text)
#     profile_image = Column(String, nullable=True)
#     date_of_birth = Column(Date(), nullable=False)
#
#     branches = relationship("Branch", secondary=doctor_branch_association, back_populates="doctors")
#
#
# class Branch(TimestampedModel, Base):
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, nullable=False)
#     description = Column(Text)
#
#     doctors = relationship("Doctor", secondary=doctor_branch_association, back_populates="branches")


class Event(TimestampedModel, Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String, nullable=False)
    description = Column(Text)
    profile_image = Column(String, nullable=True)
    ticket_quantity = Column(Integer, nullable=False)

    users = relationship("User",  back_populates="events")
    tickets = relationship("Ticket", back_populates="events")
