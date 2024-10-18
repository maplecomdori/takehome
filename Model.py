from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class QueryParam(BaseModel):
    start_date: datetime
    end_date: datetime
    phone: Optional[str] = None
    voicemail: Optional[str] = None
    user_id: Optional[str] = None
    cluster_id: Optional[str] = None


class RecordModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    originationTime: datetime
    phone: Optional[str] = None
    voicemail: Optional[str] = None
    user_id: Optional[str] = None
    cluster_id: Optional[str] = None
