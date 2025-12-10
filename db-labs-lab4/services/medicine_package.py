from typing import List, Optional

from sqlalchemy.orm import selectinload

from models.medicine_package import MedicinePackage
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest

class MedicinePackagesService:
    @staticmethod
    def get_medicine_package_by_id(id: int) -> Optional[MedicinePackage]:
        """Fetch a medicine package by ID."""
        with SessionLocal() as db:
            return db.query(MedicinePackage).options(selectinload(MedicinePackage.medicine), selectinload(MedicinePackage.package_type)).filter(MedicinePackage.id == id).first()

    @staticmethod
    def get_all_medicine_packages() -> List[MedicinePackage]:
        """Fetch all medicine packages."""
        with SessionLocal() as db:
            return db.query(MedicinePackage).options(selectinload(MedicinePackage.medicine), selectinload(MedicinePackage.package_type)).all()

    def create_medicine_package(
        self,
        medicine_id: int,
        package_type_id: int,
        quantity: int
    ) -> MedicinePackage:
        """Create a new medicine package."""
        with SessionLocal() as db:
            new_medicine_package = MedicinePackage(
                medicine_id=medicine_id,
                package_type_id=package_type_id,
                quantity=quantity
            )
            db.add(new_medicine_package)
            db.commit()
            db.refresh(new_medicine_package)
            new_medicine_package = self.get_medicine_package_by_id(new_medicine_package.id)
        return new_medicine_package

    def update_medicine_package(self, id: int, **kwargs) -> MedicinePackage:
        """Update a medicine package by ID."""
        with SessionLocal() as db:
            medicine_package = db.query(MedicinePackage).filter(MedicinePackage.id == id).first()
            if not medicine_package:
                raise NotFound(description=f"MedicinePackage with id {id} not found")
            for key, value in kwargs.items():
                setattr(medicine_package, key, value)
            db.commit()
            db.refresh(medicine_package)
            medicine_package = self.get_medicine_package_by_id(medicine_package.id)
        return medicine_package

    @staticmethod
    def delete_medicine_package(id: int) -> None:
        """Delete a medicine package by ID."""
        with SessionLocal() as db:
            medicine_package = db.query(MedicinePackage).filter(MedicinePackage.id == id).first()
            if medicine_package:
                db.delete(medicine_package)
                db.commit()
            else:
                raise NotFound(description=f"MedicinePackage with id {id} not found")