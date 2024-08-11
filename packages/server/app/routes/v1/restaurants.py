from flask import Blueprint, request, jsonify
from services.restaurant import Restaurant
from services.google import Google
from utils.calc_direction import calc_midpoint

restaurant_blueprint = Blueprint(
    "restaurant_endpoints",
    __name__,
    url_prefix="/api/restaurants",
)

@restaurant_blueprint.route("/", methods=["GET"])
def get_restaurants():
    start_place = request.args.get('start_place')
    end_place = request.args.get('end_place')
    if not start_place or not end_place:
        return jsonify({"data": None, "message": "Do not set place."})
    
    google_service = Google()
    restaurant_service = Restaurant()
    start_location, end_location = google_service.get_location(f"{start_place}", f"{end_place}")
    location_midpoint = calc_midpoint(start_location, end_location)

    restaurant_list = restaurant_service.get_restaurant_list(str(location_midpoint["lat"]), str(location_midpoint["lng"]))

    return jsonify({"data": restaurant_list, "message": "ok"})