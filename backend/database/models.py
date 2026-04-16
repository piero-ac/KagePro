from .db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CatalogModel(Base):
    __tablename__ = "catalog"
    audio_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    language = Column(String(20), nullable=False)
    duration = Column(Integer)
    s3_key = Column(String(255), nullable=False)

class SessionModel(Base):
    __tablename__ = "session"
    session_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(String, nullable=False, index=True)
    language = Column(String(20))
    date = Column(DateTime)
    duration = Column(Integer)
    activity_type = Column(String(20))

class SessionDetailsModel(Base):
    __tablename__ = "session_details"
    session_details_id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("session.session_id", ondelete="CASCADE"))
    audio_id = Column(UUID(as_uuid=True), ForeignKey("catalog.audio_id", ondelete="SET NULL"), nullable=True)
    user_audio_id = Column(String(255), nullable=True)
    title = Column(String(100), nullable=True)
    description = Column(String(300), nullable=True)