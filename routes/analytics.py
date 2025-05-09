from flask import Blueprint, jsonify

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/summary", methods=["GET"])
def summary():
    return jsonify({
        "weekly_summary": {
            "total_calories": 10500,
            "avg_per_day": 1500,
            "burned": 2500
        }
    })
