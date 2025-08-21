from flask import Flask, render_template
from config.settings import Config
from routes.chatbot_routes import chatbot_bp
from routes.report_routes import report_bp
from routes.awareness_routes import awareness_bp
from routes.helpline_routes import helpline_bp
from database.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
    app.register_blueprint(report_bp, url_prefix="/report")
    app.register_blueprint(awareness_bp, url_prefix="/news")
    app.register_blueprint(helpline_bp, url_prefix="/helpline")

    # Home route
    @app.route("/")
    def home():
        return render_template("base.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
