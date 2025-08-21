from flask import Blueprint, render_template
from core.helpline_info import helplines

helpline_bp = Blueprint("helpline", __name__)

@helpline_bp.route("/", methods=["GET"])
def helpline():
    return render_template("helpline.html", helplines=helplines)
