from flask import Flask
from routes.v1.greet import greet_blueprint
from routes.v1.restaurants import restaurant_blueprint
from flask_cors import CORS

def _register_blueprints(app: Flask):
    app.register_blueprint(greet_blueprint, url_prefix = greet_blueprint.url_prefix)
    app.register_blueprint(restaurant_blueprint, url_prefix = restaurant_blueprint.url_prefix)

def create_app() -> Flask:
    app = Flask(__name__)
    _register_blueprints(app)
    return app

if __name__ == '__main__':
    app: Flask = create_app()
    CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}})
    app.run(debug=True, host="0.0.0.0", port=8081)
