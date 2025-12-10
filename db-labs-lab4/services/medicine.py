from typing import List, Optional
from models.medicine import Medicine
from models.session import SessionLocal
from werkzeug.exceptions import NotFound, BadRequest


class MedicinesService:
    @staticmethod
    def get_medicine_by_id(id: int) -> Optional[Medicine]:
        """Fetch a medicine by ID."""
        with SessionLocal() as db:
            return db.query(Medicine).filter(Medicine.id == id).first()

    @staticmethod
    def get_all_medicines() -> List[Medicine]:
        """Fetch all medicines."""
        with SessionLocal() as db:
            return db.query(Medicine).all()

    @staticmethod
    def create_medicine(
        name: str,
        description: str,
    ) -> Medicine:
        """Create a new medicine."""
        with SessionLocal() as db:
            new_medicine = Medicine(
                name=name,
                description=description,
            )
            db.add(new_medicine)
            db.commit()
            db.refresh(new_medicine)
        return new_medicine

    @staticmethod
    def update_medicine(
        id: int,
        name: str,
        description: str
    ) -> Medicine:
        """Update a medicine."""
        with SessionLocal() as db:
            medicine = db.query(Medicine).filter(Medicine.id == id).first()
            if medicine:
                medicine.name = name
                medicine.description = description
                db.commit()
                db.refresh(medicine)
                return medicine
            else:
                raise NotFound(description=f"Medicine with id {id} not found")

    @staticmethod
    def delete_medicine(id: int) -> None:
        """Delete a medicine by ID."""
        with SessionLocal() as db:
            medicine = db.query(Medicine).filter(Medicine.id == id).first()
            if medicine:
                db.delete(medicine)
                db.commit()
            else:
                raise NotFound(description=f"Medicine with id {id} not found")