import os
from flask import Flask, app
from flask_cors import CORS
from dotenv import load_dotenv

from routes.laboratories.laboratories_routes import laboratories_bp
from routes.family.family_routes import family_bp
from routes.therapeutic_groups.therapeutic_groups_routes import therapeutic_groups_bp
from routes.potential_illnesses.potential_illness_routes import potential_illness_bp

def run_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        supports_credentials=False,
        expose_headers=["Authorization"],
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    )
    app.register_blueprint(laboratories_bp, url_prefix="/laboratories")
    app.register_blueprint(family_bp, url_prefix="/families")
    app.register_blueprint(therapeutic_groups_bp, url_prefix="/therapeutic_groups")
    app.register_blueprint(potential_illness_bp, url_prefix="/potential_illness")
    
    return app


app = run_app()

if __name__ == "__main__":
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 5000)),
        debug=True
    )