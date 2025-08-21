from flask import Blueprint, render_template, request
from core.resources_manager import fetch_cyber_news

awareness_bp = Blueprint("awareness", __name__)

@awareness_bp.route("/", methods=["GET"])
def awareness():
    query = request.args.get("q")
    news = fetch_cyber_news()
    if query:
        news = [n for n in news if query.lower() in n["title"].lower()]
    return render_template("awareness.html", news=news)
