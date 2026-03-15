from sqlalchemy import Column,String,Boolean,Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable=False)
    role = Column(String, default="Candidate")

    company_id=Column(Integer, ForeignKey("companies.id"), nullable=True)
    company=relationship("Company",back_populates="employees")

class Company(Base):
    __tablename__="companies"
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)

    employees=relationship("User",back_populates="company")

class Job(Base):
    __tablename__="jobs"
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    description=Column(String)

    company_id=Column(Integer,ForeignKey("companies.id"))
    company=relationship("Company")

class Application(Base):
    __tablename__="applications"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    job_id=Column(Integer,ForeignKey("jobs.id"))

    status=Column(String,default="pending")

    user=relationship("User")
    job=relationship("Job")