from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.db import crud,schemas,models
from app.api.deps import get_current_user
from app.db.database import get_db
from app.core.security import hash_password,verify_password,create_access_token


router=APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(user:schemas.UserCreate,db:Session=Depends(get_db)):
  
    db_user=crud.get_user_by_email(db,user.email)

    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )
    
    if not verify_password(user.password,db_user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid email or password"
        )
    
    access_token=create_access_token(
        data={"sub":str(db_user.id)}
    )

    return {
        "access_token":access_token,
        "token_type":"bearer"
    }

@router.get("/me")
def get_me(current_user:models.User=Depends(get_current_user)):
    return{
        "id":current_user.id,
        "email":current_user.email,
        "role":current_user.role
    }