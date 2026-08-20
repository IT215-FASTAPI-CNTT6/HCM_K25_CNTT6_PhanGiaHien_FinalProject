from pydantic import BaseModel
from datetime import datetime


# Schema dùng chung cho Project
class ResearchProjectBase(BaseModel):
    name: str
    description: str | None = None


# Schema tạo Project
class ResearchProjectCreate(ResearchProjectBase):
    pass


# Schema cập nhật Project
class ResearchProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


# Schema trả về Project
class ResearchProjectResponse(ResearchProjectBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Schema dùng chung cho thành viên Project
class ResearchMemberBase(BaseModel):
    user_id: int
    role: str = "MEMBER"


# Schema thêm thành viên vào Project
class ResearchMemberCreate(ResearchMemberBase):
    pass


# Schema cập nhật vai trò thành viên
class ResearchMemberUpdate(BaseModel):
    role: str | None = None


# Schema trả về thành viên Project
class ResearchMemberResponse(ResearchMemberBase):
    project_id: int
    joined_at: datetime

    class Config:
        from_attributes = True

