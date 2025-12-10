from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.session import Base

# MedicinePackage Model
class MedicinePackage(Base):
    __tablename__ = 'medicine_package'
    __table_args__ = {'schema': 'mydb'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    medicine_id = Column(Integer, ForeignKey('mydb.medicine.id'), nullable=False, index=True)
    package_type_id = Column(Integer, ForeignKey('mydb.package_type.id'), nullable=False, index=True)

    medicine = relationship("Medicine", back_populates="medicine_package", lazy="selectin")
    package_type = relationship("PackageType", back_populates="medicine_package", lazy="selectin")

    def __repr__(self):
        return (
            f"<MedicinePackage(id={self.id}, quantity={self.quantity}, medicine_id={self.medicine_id}, package_type_id={self.package_type_id})>"
        )