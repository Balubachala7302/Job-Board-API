from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db import crud,schemas,models
from app.api.deps import get_current_user

router=APIRouter(prefix="/jobs",tags=["Jobs"])

@router.post("/")
def create_job(
    job:schemas.JobCreate,
    db:Session=Depends(get_db),
    current_user:models.User=Depends(get_current_user)
):
    return crud.create_job(db=db,job=job,company_id=current_user.id)