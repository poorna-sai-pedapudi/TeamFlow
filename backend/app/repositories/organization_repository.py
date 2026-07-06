from sqlalchemy.orm import Session
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate

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