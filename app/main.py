from fastapi import FastAPI

app=FastAPI(title="Job-Board-api")

@app.get("/")
def root():
    return{"message":"Job Board api working"}

