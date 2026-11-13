from database.models.base import Base
from sqlalchemy import Integer, String, DateTime,Text
from sqlalchemy.orm import mapped_column
from datetime import datetime


class Message(Base):
    __tablename__ = "messages"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, nullable=False)
    role =mapped_column(String, nullable=False)
    content = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now, nullable=False)