from fastapi import FastAPI
from app.db.database import Base, engine

app = FastAPI(
    title = " Research Group Management API",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Khoi chay thanh cong!"
    }

