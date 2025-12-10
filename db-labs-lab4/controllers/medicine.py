from flask import Blueprint, jsonify, request
from flasgger import swag_from
from services.medicine import MedicinesService
from schemas.medicine import MedicineDTO, CreateMedicineDTO

# Define the blueprint: 'medicine', set its url prefix: /medicines
medicine_blueprint = Blueprint('medicines', __name__, url_prefix='/medicines')


@medicine_blueprint.get("/")
def get_all_medicines():
    """
    Get all medicines
    ---
    tags:
      - Medicines
    responses:
      200:
        description: A list of medicines
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "Aspirin"
              description:
                type: string
                example: "Pain reliever"
    """
    medicines = MedicinesService.get_all_medicines()
    response = [MedicineDTO.model_validate(medicine.__dict__).model_dump() for medicine in medicines]
    return jsonify(response)


@medicine_blueprint.get("/<int:id>")
def get_medicine(id: int):
    """
    Get a medicine by ID
    ---
    tags:
      - Medicines
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Medicine ID
    responses:
      200:
        description: Medicine details
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            description:
              type: string
    """
    medicine = MedicinesService.get_medicine_by_id(id=id)
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.post("/")
def create_medicine():
    """
    Create a new medicine
    ---
    tags:
      - Medicines
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - description
          properties:
            name:
              type: string
              example: "Aspirin"
            description:
              type: string
              example: "Pain reliever"
    responses:
      200:
        description: Created medicine
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            description:
              type: string
    """
    body = CreateMedicineDTO.model_validate(request.get_json())
    medicine = MedicinesService.create_medicine(
        name=body.name,
        description=body.description,
    )
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.put("/<int:id>")
def update_medicine(id: int):
    """
    Update a medicine
    ---
    tags:
      - Medicines
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Medicine ID
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - description
          properties:
            name:
              type: string
            description:
              type: string
    responses:
      200:
        description: Updated medicine
    """
    body = CreateMedicineDTO.model_validate(request.get_json())
    medicine = MedicinesService.update_medicine(
        id=id,
        name=body.name,
        description=body.description,
    )
    response = MedicineDTO.model_validate(medicine.__dict__).model_dump()
    return jsonify(response)


@medicine_blueprint.delete("/<int:id>")
def delete_medicine(id: int):
    """
    Delete a medicine
    ---
    tags:
      - Medicines
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: Medicine ID
    responses:
      200:
        description: Medicine deleted successfully
    """
    MedicinesService.delete_medicine(id=id)
    return jsonify({"detail": "medicine deleted successfully"})