from flask import Blueprint, jsonify, request

from services.medicine_package import MedicinePackagesService
from schemas.medicine_package import MedicinePackageDTO, CreateMedicinePackageDTO

# Define the blueprint: 'medicine_package', set its url prefix: /medicine_packages
medicine_package_blueprint = Blueprint('medicine_packages', __name__, url_prefix='/medicine_packages')


@medicine_package_blueprint.get("/")
def get_all_medicine_packages():
    """
    Get all medicine packages
    ---
    tags:
      - Medicine Packages
    responses:
      200:
        description: A list of medicine packages
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              medicine_id:
                type: integer
              package_type_id:
                type: integer
              quantity:
                type: integer
    """
    medicine_packages = MedicinePackagesService.get_all_medicine_packages()
    response = [MedicinePackageDTO.model_validate(medicine_package).model_dump() for medicine_package in medicine_packages]
    return jsonify(response)


@medicine_package_blueprint.get("/<int:id>")
def get_medicine_package(id: int):
    """
    Get a medicine package by ID
    ---
    tags:
      - Medicine Packages
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Medicine package details
      404:
        description: Medicine package not found
    """
    medicine_package = MedicinePackagesService.get_medicine_package_by_id(id=id)
    if not medicine_package:
        return jsonify({"detail": "Medicine package not found"}), 404
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.post("/")
def create_medicine_package():
    """
    Create a new medicine package
    ---
    tags:
      - Medicine Packages
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - medicine_id
            - package_type_id
            - quantity
          properties:
            medicine_id:
              type: integer
              example: 1
            package_type_id:
              type: integer
              example: 1
            quantity:
              type: integer
              example: 100
    responses:
      200:
        description: Created medicine package
    """
    body = CreateMedicinePackageDTO.model_validate(request.get_json())
    medicine_package = MedicinePackagesService().create_medicine_package(
        medicine_id=body.medicine_id,
        package_type_id=body.package_type_id,
        quantity=body.quantity
    )
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.put("/<int:id>")
def update_medicine_package(id: int):
    """
    Update a medicine package
    ---
    tags:
      - Medicine Packages
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            medicine_id:
              type: integer
            package_type_id:
              type: integer
            quantity:
              type: integer
    responses:
      200:
        description: Updated medicine package
    """
    body = CreateMedicinePackageDTO.model_validate(request.get_json())
    medicine_package = MedicinePackagesService().update_medicine_package(
        id=id,
        medicine_id=body.medicine_id,
        package_type_id=body.package_type_id,
        quantity=body.quantity
    )
    response = MedicinePackageDTO.model_validate(medicine_package).model_dump()
    return jsonify(response)


@medicine_package_blueprint.delete("/<int:id>")
def delete_medicine_package(id: int):
    """
    Delete a medicine package
    ---
    tags:
      - Medicine Packages
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Medicine package deleted successfully
    """
    MedicinePackagesService.delete_medicine_package(id=id)
    return jsonify({"detail": "medicine package deleted successfully"})