from flask_swagger_ui import get_swaggerui_blueprint

swaggerui_blueprint = get_swaggerui_blueprint(
    '/api/docs',
    '/swagger.json',
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    }
)