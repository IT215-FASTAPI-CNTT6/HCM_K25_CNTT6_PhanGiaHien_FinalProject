
#  Schema dùng chung cho Project
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class ResearchProjectBase(BaseModel):

    name: str = Field(
        min_length=1,
        max_length=255
    )

    description: str | None = None


class ResearchProjectCreate(ResearchProjectBase):
    pass


class ResearchProjectUpdate(BaseModel):

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255
    )

    description: str | None = None


class ResearchProjectResponse(ResearchProjectBase):

    id: int
    owner_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


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

        

