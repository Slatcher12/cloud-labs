from flask import Blueprint, jsonify, request
from services.package_type import PackageTypesService
from schemas.package_type import PackageTypeDTO, CreatePackageTypeDTO

# Define the blueprint: 'package_type', set its url prefix: /package_types
package_type_blueprint = Blueprint('package_types', __name__, url_prefix='/package_types')


@package_type_blueprint.get("/")
def get_all_package_types():
    """
    Get all package types
    ---
    tags:
      - Package Types
    responses:
      200:
        description: A list of package types
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              type:
                type: string
              description:
                type: string
    """
    package_types = PackageTypesService.get_all_package_types()
    response = [PackageTypeDTO.model_validate(package_type.__dict__).model_dump() for package_type in package_types]
    return jsonify(response)


@package_type_blueprint.get("/<int:id>")
def get_package_type(id: int):
    """
    Get a package type by ID
    ---
    tags:
      - Package Types
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Package type details
    """
    package_type = PackageTypesService.get_package_type_by_id(id=id)
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.post("/")
def create_package_type():
    """
    Create a new package type
    ---
    tags:
      - Package Types
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - type
            - description
          properties:
            type:
              type: string
              example: "Bottle"
            description:
              type: string
              example: "Bottle packaging"
    responses:
      200:
        description: Created package type
    """
    body = CreatePackageTypeDTO.model_validate(request.get_json())
    package_type = PackageTypesService.create_package_type(
        type=body.type,
        description=body.description
    )
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.put("/<int:id>")
def update_package_type(id: int):
    """
    Update a package type
    ---
    tags:
      - Package Types
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
            type:
              type: string
            description:
              type: string
    responses:
      200:
        description: Updated package type
    """
    body = CreatePackageTypeDTO.model_validate(request.get_json())
    package_type = PackageTypesService.update_package_type(
        id=id,
        type=body.type,
        description=body.description
    )
    response = PackageTypeDTO.model_validate(package_type.__dict__).model_dump()
    return jsonify(response)


@package_type_blueprint.delete("/<int:id>")
def delete_package_type(id: int):
    """
    Delete a package type
    ---
    tags:
      - Package Types
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Package type deleted successfully
    """
    PackageTypesService.delete_package_type(id=id)
    return jsonify({"detail": "package type deleted successfully"})