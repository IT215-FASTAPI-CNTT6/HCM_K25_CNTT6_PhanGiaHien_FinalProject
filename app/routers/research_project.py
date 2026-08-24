from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.research_project import (
    ResearchProjectCreate,
    ResearchProjectResponse
)
from app.services.research_project_service import (
    create_research_project,
    get_research_projects
)


router = APIRouter(
    prefix="/research-projects",
    tags=["Research Projects"]
)


@router.post(
    "",
    response_model=ResearchProjectResponse,
    status_code=status.HTTP_201_CREATED
)
def create_project(
    project_data: ResearchProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = create_research_project(
        project_data=project_data,
        owner_id=current_user.id,
        db=db
    )

    return project


@router.get(
    "",
    response_model=list[ResearchProjectResponse]
)
def get_projects(
    search: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    projects = get_research_projects(
        user_id=current_user.id,
        search=search,
        db=db
    )

    return projects
