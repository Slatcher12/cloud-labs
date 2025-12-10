# app.py
from flask import Flask
from flasgger import Swagger

from controllers.medicine import medicine_blueprint
from controllers.medicine_package import medicine_package_blueprint
from controllers.package_type import package_type_blueprint

app = Flask(__name__)

# Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Medicine API",
        "description": "API for managing medicines, package types, and medicine packages",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http", "https"]
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

# Register the user blueprint
app.register_blueprint(medicine_blueprint)
app.register_blueprint(package_type_blueprint)
app.register_blueprint(medicine_package_blueprint)


@app.route('/')
def index():
    return "Welcome to the Flask app with Blueprints!", 200


if __name__ == '__main__':
    app.run(debug=True)
