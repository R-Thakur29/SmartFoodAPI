from flask import Blueprint, request, jsonify

recipes_bp = Blueprint("recipes", __name__)

@recipes_bp.route("/", methods=["GET"])
def get_recipes():
    ingredients = request.args.get("ingredients", "egg,tomato")
    return jsonify({
        "ingredients_used": ingredients.split(","),
        "recipes": [
            {"name": "Tomato Egg Curry", "calories": 220},
            {"name": "Spicy Scrambled Eggs", "calories": 180}
        ]
    })
