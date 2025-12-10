from typing import List, Optional
from models.package_type import PackageType
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest


class PackageTypesService:
    @staticmethod
    def get_package_type_by_id(id: int) -> Optional[PackageType]:
        """Fetch a package type by ID."""
        with SessionLocal() as db:
            return db.query(PackageType).filter(PackageType.id == id).first()

    @staticmethod
    def get_all_package_types() -> List[PackageType]:
        """Fetch all package types."""
        with SessionLocal() as db:
            return db.query(PackageType).all()

    @staticmethod
    def create_package_type(
        type: str,
        description: str
    ) -> PackageType:
        """Create a new package type."""
        with SessionLocal() as db:
            new_package_type = PackageType(
                type=type,
                description=description
            )
            db.add(new_package_type)
            db.commit()
            db.refresh(new_package_type)
        return new_package_type

    @staticmethod
    def update_package_type(
        id: int,
        type: str,
        description: str
    ) -> PackageType:
        """Update a package type."""
        with SessionLocal() as db:
            package_type = db.query(PackageType).filter(PackageType.id == id).first()
            if package_type:
                package_type.type = type
                package_type.description = description
                db.commit()
                db.refresh(package_type)
                return package_type
            else:
                raise NotFound(description=f"PackageType with id {id} not found")

    @staticmethod
    def delete_package_type(id: int) -> None:
        """Delete a package type by ID."""
        with SessionLocal() as db:
            package_type = db.query(PackageType).filter(PackageType.id == id).first()
            if package_type:
                db.delete(package_type)
                db.commit()
            else:
                raise NotFound(description=f"PackageType with id {id} not found")