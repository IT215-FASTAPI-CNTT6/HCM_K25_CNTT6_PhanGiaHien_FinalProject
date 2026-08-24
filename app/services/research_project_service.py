from sqlalchemy.orm import Session

from app.models.research_project import (
    ResearchProject,
    ResearchMember
)
from app.schemas.research_project import (
    ResearchProjectCreate
)


def create_research_project(
    project_data: ResearchProjectCreate,
    owner_id: int,
    db: Session
):

    project = ResearchProject(
        name=project_data.name,
        description=project_data.description,
        owner_id=owner_id
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    owner_member = ResearchMember(
        project_id=project.id,
        user_id=owner_id,
        role="OWNER"
    )

    db.add(owner_member)
    db.commit()

    return project
