from pydantic import BaseModel
from datetime import datetime


# Schema dùng chung cho Task
class ResearchTaskBase(BaseModel):
    title: str
    description: str | None = None
    priority: str = "MEDIUM"
    due_date: datetime | None = None


# Schema tạo Task
class ResearchTaskCreate(ResearchTaskBase):
    assignee_id: int | None = None


# Schema cập nhật Task
class ResearchTaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    assignee_id: int | None = None
    status: str | None = None
    priority: str | None = None
    due_date: datetime | None = None


# Schema trả về Task
class ResearchTaskResponse(ResearchTaskBase):
    id: int
    project_id: int
    assignee_id: int | None = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
