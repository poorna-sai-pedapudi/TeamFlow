from fastapi import APIRouter, Depends, status, HTTPException
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


@router.get(
    "",
    response_model=list[OrganizationResponse],
)
def get_organizations(
    db: Session = Depends(get_db),
):
    repository = OrganizationRepository()
    return repository.get_all(db=db)

@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse,
)
def get_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):
    repository = OrganizationRepository()

    organization = repository.get_by_id(
        db=db,
        organization_id=organization_id
    )

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )
    
    return organization