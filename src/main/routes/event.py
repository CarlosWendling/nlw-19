from flask import Blueprint, jsonify # type: ignore

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/event", methods=["POST"])
def create_new_event ():
    return jsonify({ "estou": "aqui" }), 201