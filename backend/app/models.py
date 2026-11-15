from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, text
from .database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    long_url = Column(Text, nullable=False)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))