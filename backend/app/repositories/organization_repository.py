from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
)

class OrganizationRepository:

    def create(
            self,
            db: Session,
            organization: OrganizationCreate,
    ) -> Organization:
        
        db_organization = Organization(
            name = organization.name,
        )

        db.add(db_organization)
        db.commit()
        db.refresh(db_organization)

        return db_organization
    
    def get_all(self, db: Session) -> list[Organization]:
        return db.query(Organization).all()
    
    def get_by_id(self, db: Session, organization_id: int) -> Organization | None:
        return (
            db.query(Organization)
            .filter(Organization.id == organization_id)
            .first()
        )
    
    def update(
    self,
    db: Session,
    organization: Organization,
    organization_update: OrganizationUpdate,
) -> Organization:

        organization.name = organization_update.name

        db.commit()
        db.refresh(organization)

        return organization