from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field
from enum import Enum

class ActivityType(str, Enum):
    shadowing = "shadowing"
    reading = "reading"
    writing = "writing"
    listening = "listening"
    online_tutoring = "online_tutoring"

class SessionCreate(BaseModel):
    language: str = Field(min_length=2, max_length=20)
    date: datetime
    duration: int
    activity_type: ActivityType

class SessionResponse(BaseModel):
    session_id: UUID
    user_id: str
    language: str
    date: datetime
    duration: int
    activity_type: str

    class Config:
        from_attributes = True

class SessionDetailsCreate(BaseModel):
    audio_id: str | None = None
    user_audio_id: str | None = None
    title: str | None = None
    description: str | None = None

class SessionDetailsResponse(BaseModel):
    session_details_id: UUID
    session_id: UUID
    audio_id: str | None
    user_audio_id: str | None
    title: str | None
    description: str | None

    class Config:
        from_attributes = True