import datetime

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from utils import auth

router = APIRouter(
    prefix="/immersion",
    tags=["immersion"],
)

class ShadowActivity(BaseModel):
    type: str
    date: str
    shadow_audio_id: str
    user_shadow_audio_id: str



@router.get("/history")
async def my_shadowing_history(request: Request):
    user_details = auth.authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")

    return {"history" : []}