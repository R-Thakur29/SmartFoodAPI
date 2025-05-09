from flask import Flask
from routes.recipes import recipes_bp
from routes.nutrition import nutrition_bp
from routes.profile import profile_bp
from routes.recommendations import recommendations_bp
from routes.analytics import analytics_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(recipes_bp, url_prefix="/recipes")
app.register_blueprint(nutrition_bp, url_prefix="/nutrition")
app.register_blueprint(profile_bp, url_prefix="/user")
app.register_blueprint(recommendations_bp, url_prefix="/recommendations")
app.register_blueprint(analytics_bp, url_prefix="/analytics")

@app.route("/")
def home():
    return {"message": "SmartFood API Platform is Live!"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
