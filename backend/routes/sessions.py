from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Request, status
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.models import SessionModel, SessionDetailsModel
from database.db import get_db
from models.session import SessionCreate, SessionDetailsCreate

# from ..utils import auth
#   user_details = auth.authenticate_and_get_user_details(request)
# user_id = user_details.get("user_id")

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
)

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
async def get_sessions(request: Request):
    return "Sessions Endpoint"

@router.get("/{session_id}")
async def get_session(db:db_dependency, session_id: UUID):
    # TODO: check for valid user
    result = db.execute(
        select(SessionModel)
        .where(SessionModel.session_id == session_id)
        .filter(SessionModel.user_id == "user_test_123") # get user id from clerk auth
    )
    session = result.scalars().first()
    return session

@router.get("/{session_id}/details")
async def get_session_details(db:db_dependency, session_id: UUID):
    # TODO: check for valid user
    result = db.execute(
        select(SessionDetailsModel)
        .where(SessionDetailsModel.session_id == session_id)
    )
    session_details = result.scalars().first()
    return session_details

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_session(db:db_dependency, session_request: SessionCreate):
    # TODO: check for valid user

    session_model = SessionModel(**session_request.model_dump(), user_id="user_test_123") # change with clerk user id
    db.add(session_model)
    db.commit()
    db.refresh(session_model)
    return {"session_id": session_model.session_id}

@router.post("/{session_id}/details", status_code=status.HTTP_201_CREATED)
async def create_session_details(db:db_dependency, session_id: UUID, session_details_request: SessionDetailsCreate):
    # TODO: check for valid user

    session = db.execute(
        select(SessionModel)
        .where(SessionModel.session_id == session_id)
        .filter(SessionModel.user_id == "user_test_123")
    ).scalars().first()

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    session_details_model = SessionDetailsModel(**session_details_request.model_dump())
    session_details_model.session_id = session_id
    db.add(session_details_model)
    db.commit()
    db.refresh(session_details_model)
    return {"session_details_id": session_details_model.session_details_id}

