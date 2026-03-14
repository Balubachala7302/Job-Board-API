from sqlalchemy import Column,String,Boolean,Integer
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    role = Column(String, default="Candidate")