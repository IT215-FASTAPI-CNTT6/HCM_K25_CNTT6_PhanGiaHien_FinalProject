from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.database import Base


class ResearchTask(Base):
    """Bảng lưu các công việc thuộc từng dự án nghiên cứu."""

    __tablename__ = "research_tasks"

    id = Column(Integer, primary_key=True, index=True)

    # Task thuộc về project nào
    project_id = Column(
        Integer,
        ForeignKey("research_projects.id"),
        nullable=False
    )

    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)

    # Người được giao task, có thể để trống
    assignee_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=True
    )

    # Trạng thái và mức độ ưu tiên
    status = Column(String(20), default="TODO", nullable=False)
    priority = Column(String(20), default="MEDIUM", nullable=False)

    due_date = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )

    # Relationship với Project
    project = relationship(
        "ResearchProject",
        back_populates="tasks"
    )

    # Relationship với User
    assignee = relationship(
        "User",
        back_populates="assigned_tasks",
        foreign_keys=[assignee_id]
    )
