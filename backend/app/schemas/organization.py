from datetime import datetime
from pydantic import BaseModel, Field

class OrganizationCreate(BaseModel):
    name: str = Field(..., min_length = 2, max_length = 255)

class OrganizationResponse(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True


class OrganizationUpdate(BaseModel):
    name: str = Field(..., min_length = 2, max_length = 255)