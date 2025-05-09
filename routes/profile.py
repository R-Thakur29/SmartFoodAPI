from flask import Blueprint, jsonify

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["GET"])
def get_profile():
    return jsonify({
        "user_id": 1,
        "age": 25,
        "diet": "vegetarian",
        "goals": "muscle gain"
    })
