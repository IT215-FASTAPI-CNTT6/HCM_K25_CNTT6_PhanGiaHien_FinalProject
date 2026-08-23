from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base


class ResearchProject(Base):
    """Bảng lưu thông tin các dự án nghiên cứu."""

    __tablename__ = "research_projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)

    # Khóa ngoại: mỗi project có một người sở hữu
    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    # Quan hệ ngược lại với User
    owner = relationship(
        "User",
        back_populates="owned_projects",
        foreign_keys=[owner_id]
    )

    # Một project có nhiều thành viên
    members = relationship(
        "ResearchMember",
        back_populates="project"
    )

    # Một project có nhiều task
    tasks = relationship(
        "ResearchTask",
        back_populates="project"
    )


class ResearchMember(Base):
    __tablename__ = "research_members"

    # cùng một user không thể tham gia cùng một project nhiều lần
    __table_args__ = (
        UniqueConstraint(
            "project_id",
            "user_id",
            name="uq_research_member_project_user"
        ),
    )

    project_id = Column(
        Integer,
        ForeignKey("research_projects.id"),
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        primary_key=True
    )

    # Vai trò của thành viên trong project
    role = Column(String(20), default="MEMBER", nullable=False)

    joined_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    # Relationship hai chiều
    project = relationship(
        "ResearchProject",
        back_populates="members"
    )

    user = relationship(
        "User",
        back_populates="memberships"
    )
