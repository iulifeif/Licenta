from sqlalchemy import Column, ForeignKey, Integer, PrimaryKeyConstraint
from src.models.base import Base


class UserSchool(Base):
    __tablename__ = 'user_school'
    __table_args__ = (PrimaryKeyConstraint('user_id', 'school_id'),)

    user_id = Column(Integer, ForeignKey("user.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    school_id = Column(Integer, ForeignKey("school.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
