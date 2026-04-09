from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from typing import Annotated
from sqlalchemy.orm import Session
from routes import sessions
from database.db import get_db

db_dependency = Annotated[Session, Depends(get_db)]

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"]
                )

app.include_router(sessions.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check(db: db_dependency):
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
