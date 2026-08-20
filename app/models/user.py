from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    # Thông tin cơ bản của người dùng
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    full_name = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)

    # Vai trò trong hệ thống
    role = Column(String(20), default="USER", nullable=False)

    # Trạng thái hoạt động
    is_active = Column(Boolean, default=True)

    # Thời gian tạo
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    # Quan hệ:
    # user.owned_projects -> các project do user làm chủ
    # user.memberships    -> các project mà user tham gia
    # user.assigned_tasks -> các task được giao cho user
    owned_projects = relationship(
        "ResearchProject",
        back_populates="owner",
        foreign_keys="ResearchProject.owner_id"
    )

    memberships = relationship(
        "ResearchMember",
        back_populates="user"
    )

    assigned_tasks = relationship(
        "ResearchTask",
        back_populates="assignee",
        foreign_keys="ResearchTask.assignee_id"
    )
