from flask import Blueprint, render_template, request, send_file
from database.models import db, Report
from core.report_generator import generate_pdf, generate_docx
import os

report_bp = Blueprint("report", __name__)

@report_bp.route("/", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        data = {
            "Name": request.form["name"],
            "Email": request.form["email"],
            "Phone": request.form["phone"],
            "Incident": request.form["incident"],
            "Description": request.form["description"],
            "Location": request.form["location"],
            "Date": request.form["date"]
        }

        # Save in DB
        report_entry = Report(**data)
        db.session.add(report_entry)
        db.session.commit()

        # Generate files
        pdf_file = generate_pdf(data)
        docx_file = generate_docx(data)

        return send_file(pdf_file, as_attachment=True)

    return render_template("report_form.html")
