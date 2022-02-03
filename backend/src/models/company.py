from sqlalchemy import Column, String, Integer
from src.models.base import Base


class School(Base):
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    street = Column(String(200))
    city = Column(String(100))
