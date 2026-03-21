from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.api import users
from app.api import auth,jobs,applications


models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="Job-Board-api")

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(applications.router)

@app.get("/")
def root():
    return{"message":"Job Board api working"}

