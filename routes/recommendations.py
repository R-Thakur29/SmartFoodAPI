from flask import Blueprint, jsonify

recommendations_bp = Blueprint("recommendations", __name__)

@recommendations_bp.route("/", methods=["GET"])
def recommend():
    return jsonify({
        "meal_plan": [
            {"day": "Monday", "recipe": "Paneer Wrap"},
            {"day": "Tuesday", "recipe": "Grilled Veggie Bowl"}
        ]
    })
