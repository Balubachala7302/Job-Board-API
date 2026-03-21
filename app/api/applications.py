from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db import crud,schemas,models
from app.api.deps import get_current_user

router=APIRouter(prefix="/applications",tags=["Applications"])

@router.post("/")
def apply_job(
    job_id:int,
    db:Session=Depends(get_db),
    current_user:models.User=Depends(get_current_user)

):
    application=crud.apply_job(
        db=db,
        user_id=current_user.id,
        job_id=job_id
    )

    if not application:
        raise HTTPException(
            status_code=400,
            detail="Already applied for this job"
        )
    
    return application

@router.get("/me")
def my_applications(
    db:Session=Depends(get_db),
    current_user:models.User=Depends(get_current_user)
):
    return db.query(models.Application).filter(models.Application.user_id==current_user.id).all()

