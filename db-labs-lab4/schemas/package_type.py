from pydantic import BaseModel


class PackageTypeBase(BaseModel):
    type: str
    description: str

    class Config:
        from_attributes = True


class CreatePackageTypeDTO(PackageTypeBase):
    pass


class PackageTypeDTO(PackageTypeBase):
    id: int
