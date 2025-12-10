from pydantic import BaseModel


class MedicineBase(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True


class CreateMedicineDTO(MedicineBase):
    pass


class MedicineDTO(MedicineBase):
    id: int
