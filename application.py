import json
from flask import Flask, request, jsonify
from app.routes.user import user
from app.routes.admin import admin
from app.routes.swagger import swaggerui_blueprint

app = Flask(__name__, static_url_path='')

app.register_blueprint(user, url_prefix='/api/users')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(swaggerui_blueprint, url_prefix='/api/docs')

@app.route('/')
def index():
    return 'index'

# @app.route('/api/spec')
# def api_spec():
#     template = {}
#     with open("./swagger.json", "r") as f:
#         template = json.loads(f.read())

#     print(template)
#     return '1'
#     # return jsonify(swagger(app, _sanitize, template))


if __name__ == "__main__":
    app.run()