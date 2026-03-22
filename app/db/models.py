from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


# -------------------------
# USER
# -------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="candidate")  # candidate / company / admin

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    company = relationship("Company", back_populates="employees")
    applications = relationship("Application", back_populates="user")

    created_at = Column(DateTime, default=datetime.utcnow)


# -------------------------
# COMPANY
# -------------------------
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

    employees = relationship("User", back_populates="company")
    jobs = relationship("Job", back_populates="company")

    created_at = Column(DateTime, default=datetime.utcnow)


# -------------------------
# JOB
# -------------------------
class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)

    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="jobs")
    applications = relationship("Application", back_populates="job")

    created_at = Column(DateTime, default=datetime.utcnow)


# -------------------------
# APPLICATION
# -------------------------
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    status = Column(String, default="pending")  # pending / accepted / rejected

    user = relationship("User", back_populates="applications")
    job = relationship("Job", back_populates="applications")

    created_at = Column(DateTime, default=datetime.utcnow)