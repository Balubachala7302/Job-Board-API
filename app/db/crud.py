from sqlalchemy.orm import Session
from app.db import models, schemas
from app.core.security import hash_password


# -------------------------
# USER
# -------------------------
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),  # ✅ FIXED
        role="user"  # default role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# -------------------------
# COMPANY
# -------------------------
def create_company(db: Session, company: schemas.CompanyCreate):
    db_company = models.Company(
        name=company.name,
        description=company.description
    )

    db.add(db_company)
    db.commit()
    db.refresh(db_company)

    return db_company


# -------------------------
# JOB
# -------------------------
def create_job(db: Session, job: schemas.JobCreate, company_id: int):
    db_job = models.Job(   # ✅ FIXED (capital J)
        title=job.title,
        description=job.description,
        location=job.location,
        company_id=company_id
    )

    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    return db_job


def get_jobs(db: Session):
    return db.query(models.Job).all()


# -------------------------
# APPLICATION
# -------------------------
def apply_job(db: Session, user_id: int, job_id: int):

    # ❗ Prevent duplicate applications
    existing = db.query(models.Application).filter(
        models.Application.user_id == user_id,
        models.Application.job_id == job_id
    ).first()

    if existing:
        return None

    application = models.Application(
        user_id=user_id,
        job_id=job_id,
        status="pending"
    )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application