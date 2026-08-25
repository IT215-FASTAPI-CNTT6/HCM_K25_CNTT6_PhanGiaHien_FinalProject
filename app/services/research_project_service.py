from sqlalchemy.orm import Session

from app.models.research_project import (
    ResearchProject,
    ResearchMember
)
from app.schemas.research_project import (
    ResearchProjectCreate,
    ResearchProjectUpdate
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


def get_research_projects(
    user_id: int,
    search: str | None,
    db: Session
):

    query = db.query(ResearchProject).join(
        ResearchMember
    ).filter(
        ResearchMember.user_id == user_id
    )

    if search:
        query = query.filter(
            ResearchProject.name.contains(search)
        )

    return query.all()


def get_research_project(
    project_id: int,
    user_id: int,
    db: Session
):

    project = db.query(ResearchProject).filter(
        ResearchProject.id == project_id
    ).first()

    if project is None:
        return None

    member = db.query(ResearchMember).filter(
        ResearchMember.project_id == project_id,
        ResearchMember.user_id == user_id
    ).first()

    if member is None:
        return None

    return project


def update_research_project(
    project_id: int,
    project_data: ResearchProjectUpdate,
    user_id: int,
    db: Session
):

    project = db.query(ResearchProject).filter(
        ResearchProject.id == project_id
    ).first()

    if project is None:
        return None

    if project.owner_id != user_id:
        return "FORBIDDEN"

    if project_data.name is not None:
        project.name = project_data.name

    if project_data.description is not None:
        project.description = project_data.description

    db.commit()
    db.refresh(project)

    return project


def delete_research_project(
    project_id: int,
    user_id: int,
    db: Session
):

    project = db.query(ResearchProject).filter(
        ResearchProject.id == project_id
    ).first()

    if project is None:
        return None

    if project.owner_id != user_id:
        return "FORBIDDEN"

    db.delete(project)
    db.commit()

    return True
