from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
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
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(current_user:models.User=Depends(get_current_user)):
    return{
        "id":current_user.id,
        "email":current_user.email,
        "role":current_user.role
    }