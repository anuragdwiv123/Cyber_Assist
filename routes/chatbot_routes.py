from flask import Blueprint, render_template, request
from core.chatbot_engine import get_response
from database.models import db, ChatLog

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/", methods=["GET", "POST"])
def chatbot():
    reply = None
    if request.method == "POST":
        user_msg = request.form["message"]
        reply = get_response(user_msg)

        # Save to DB
        log = ChatLog(user_message=user_msg, bot_reply=reply)
        db.session.add(log)
        db.session.commit()

    return render_template("chatbot.html", reply=reply)
