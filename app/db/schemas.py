from pydantic import BaseModel
from typing import Optional


# ----------------------
# USER
# ----------------------
class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True


# ----------------------
# COMPANY
# ----------------------
class CompanyCreate(BaseModel):
    name: str
    description: Optional[str] = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True


# ----------------------
# JOB
# ----------------------
class JobCreate(BaseModel):
    title: str
    description: str
    location: str


class JobResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str

    class Config:
        from_attributes = True


# ----------------------
# APPLICATION
# ----------------------
class ApplicationCreate(BaseModel):
    job_id: int


class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    status: str   # fixed

    class Config:
        from_attributes = True