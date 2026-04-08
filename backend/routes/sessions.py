from fastapi import APIRouter, Depends, HTTPException, Request
from ..utils import auth

# from ..utils import auth
#   user_details = auth.authenticate_and_get_user_details(request)
# user_id = user_details.get("user_id")

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"],
)

@router.get("/")
async def get_sessions(request: Request):
    return "Sessions Endpoint"

@router.get("/{session_id}")
async def get_session(request: Request, session_id: str):
    return {session_id: session_id}

@router.get("/{session_id}/details")
async def get_session_details(request: Request, session_id: str):
    return {session_id: session_id}