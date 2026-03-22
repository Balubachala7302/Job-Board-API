from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


# ----------------------
# USER
# ----------------------
class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    role: str
    created_at: datetime

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
    created_at: datetime

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
    company_id: int
    created_at: datetime

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
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


# ----------------------
# PAGINATION (🔥 IMPORTANT)
# ----------------------
class PaginationMeta(BaseModel):
    total: int
    page: int
    limit: int
    total_pages: int


class PaginatedJobResponse(BaseModel):
    meta: PaginationMeta
    data: List[JobResponse]


class PaginatedApplicationResponse(BaseModel):
    meta: PaginationMeta
    data: List[ApplicationResponse]