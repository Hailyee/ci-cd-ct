#실제서버코드

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Mobis! CI/CD/CT Pipeline is working!"}