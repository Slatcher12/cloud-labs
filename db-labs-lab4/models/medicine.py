from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from models.session import Base

# Medicine Model
class Medicine(Base):
    __tablename__ = 'medicine'
    __table_args__ = {'schema': 'mydb'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)

    # Define the relationship to MedicinePackage
    medicine_package = relationship('MedicinePackage', back_populates='medicine', lazy='selectin')

    def __repr__(self):
        return (
            f"<Medicine(id={self.id}, name='{self.name}', description='{self.description}')>"
        )