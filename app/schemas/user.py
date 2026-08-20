from pydantic import BaseModel, EmailStr
from datetime import datetime


# Schema dùng chung
class UserBase(BaseModel):
    email: EmailStr
    full_name: str


# Schema tạo mới User
class UserCreate(UserBase):
    password: str


# Schema cập nhật User
class UserUpdate(BaseModel):
    full_name: str | None = None
    is_active: bool | None = None


# Schema trả về cho client
class UserResponse(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        # Cho phép Pydantic đọc dữ liệu trực tiếp từ SQLAlchemy Model
        from_attributes = True
