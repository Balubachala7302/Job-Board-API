from fastapi import FastAPI
from app.db.database import engine
from app.db import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="Job-Board-api")

@app.get("/")
def root():
    return{"message":"Job Board api working"}

