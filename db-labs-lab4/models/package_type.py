from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from models.session import Base

# PackageType Model
class PackageType(Base):
    __tablename__ = 'package_type'
    __table_args__ = {'schema': 'mydb'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)

    # Define the relationship to MedicinePackage
    medicine_package = relationship('MedicinePackage', back_populates='package_type', lazy='selectin')

    def __repr__(self):
        return (
            f"<PackageType(id={self.id}, type='{self.type}', description='{self.description}')>"
        )