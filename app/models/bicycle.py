from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Bicycle(Base):
    __tablename__ = "bicycles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    starting_bid = Column(Float)
    highest_bid = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="bicycles")
    bids = relationship("Bid", back_populates="bicycle")
