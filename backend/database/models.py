from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Session(Base):
    __tablename__ = "session"
    session_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(String, index=True)
    language = Column(String)
    date = Column(DateTime)
    duration = Column(Integer)
    activity_type = Column(String)

class SessionDetails(Base):
    __tablename__ = "session_details"
    session_details_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    audio_id = Column(String)
    user_audio_id = Column(String)
    title = Column(String)
    description = Column(String)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.session_id"))