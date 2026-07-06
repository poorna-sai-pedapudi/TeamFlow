from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.repositories.organization_repository import OrganizationRepository
from app.schemas.organization import OrganizationCreate, OrganizationResponse

router = APIRouter(
    prefix = "/organizations",
    tags = ["Organizations"],
)

@router.post(
    "",
    response_model=OrganizationResponse,
    status_code=status.HTTP_201_CREATED,
)

def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):
    
    repository = OrganizationRepository()
    return repository.create(db=db, organization=organization)