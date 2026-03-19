from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name:str
    email:str

class UserCreate(BaseModel):
    email:str
    password:str

class UserResponse(BaseModel):
    id:str
    role:str

    class Config:
        from_attributes=True

class CompanyCreate(BaseModel):
    name:str
    description:Optional[str]=None

class CompanyResponse(BaseModel):
    id:int
    name:str
    description:Optional[str]

    class Config:
        from_atttributes=True

class JobCreate(BaseModel):
    title:str
    description:str
    location:str

class JobResponse(BaseModel):
    id:int
    title:str
    description:str
    location:str

    class Config:
        from_attributes=True

class ApplicationCreate(BaseModel):
    job_id:int

class ApplicationResponse(BaseModel):
    id:int
    user_id:int
    job_id:int
    status:int

    class Config:
        from_attributes=True


