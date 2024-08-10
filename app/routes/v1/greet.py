from flask import Blueprint, jsonify

greet_blueprint = Blueprint(
    "greet_endpoints",
    __name__,
    url_prefix="/api/greet",
)

@greet_blueprint.route("/", methods=["GET"])
def greet():
    return jsonify({"message": "Hello World"})
