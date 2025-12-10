from typing import List
from pydantic import BaseModel

from models.medicine_package import MedicinePackage
from models.package_type import PackageType
from schemas.medicine import MedicineDTO
from schemas.package_type import PackageTypeDTO


class MedicinePackageBase(BaseModel):
    quantity: int

    class Config:
        from_attributes = True


class CreateMedicinePackageDTO(MedicinePackageBase):
    medicine_id: int
    package_type_id: int


class MedicinePackageLessDTO(MedicinePackageBase):
    id: int


class MedicinePackageDTO(MedicinePackageBase):
    id: int
    medicine: MedicineDTO
    package_type: PackageTypeDTO


class MedicineWithMedicinePackageDTO(MedicinePackageDTO):
    medicine_packages: List[MedicinePackageLessDTO]


class MedicineWithPackageTypeDTO(PackageTypeDTO):
    medicine_packages: List[MedicinePackageLessDTO]