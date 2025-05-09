from flask import Blueprint, request, jsonify

nutrition_bp = Blueprint("nutrition", __name__)

@nutrition_bp.route("/", methods=["GET"])
def get_nutrition():
    item = request.args.get("item", "apple")
    return jsonify({
        "item": item,
        "nutrition": {
            "calories": 95,
            "protein": "0.5g",
            "carbs": "25g",
            "fiber": "4g"
        }
    })
