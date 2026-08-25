from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.research_project import (
    ResearchProjectCreate,
    ResearchProjectUpdate,
    ResearchProjectResponse
)
from app.services.research_project_service import (
    create_research_project,
    get_research_projects,
    get_research_project,
    update_research_project,
    delete_research_project
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


@router.get(
    "/{project_id}",
    response_model=ResearchProjectResponse
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_research_project(
        project_id=project_id,
        user_id=current_user.id,
        db=db
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research project not found"
        )

    return project


@router.patch(
    "/{project_id}",
    response_model=ResearchProjectResponse
)
def update_project(
    project_id: int,
    project_data: ResearchProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = update_research_project(
        project_id=project_id,
        project_data=project_data,
        user_id=current_user.id,
        db=db
    )

    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research project not found"
        )

    if project == "FORBIDDEN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only owner can update research project"
        )

    return project


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    result = delete_research_project(
        project_id=project_id,
        user_id=current_user.id,
        db=db
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Research project not found"
        )

    if result == "FORBIDDEN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only owner can delete research project"
        )
