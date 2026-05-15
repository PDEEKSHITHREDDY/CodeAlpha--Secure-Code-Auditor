from flask import Flask, render_template, request, redirect, url_for
from flask import send_file
import os
import json

from datetime import datetime

from scanner.scanner import run_bandit_scan

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


def calculate_stats(report):

    high = 0
    medium = 0
    low = 0

    if "results" in report:

        for issue in report["results"]:

            severity = issue["issue_severity"]

            if severity == "HIGH":
                high += 1

            elif severity == "MEDIUM":
                medium += 1

            elif severity == "LOW":
                low += 1

    total = high + medium + low

    score = max(100 - (high * 25 + medium * 15 + low * 5), 0)

    return total, high, medium, low, score


@app.route("/")
def home():

    report_path = os.path.join(REPORT_FOLDER, "report.json")

    total = high = medium = low = score = 0

    if os.path.exists(report_path):

        with open(report_path, "r") as f:
            report = json.load(f)

        total, high, medium, low, score = calculate_stats(report)

    return render_template(
        "index.html",
        total=total,
        high=high,
        medium=medium,
        low=low,
        score=score
    )


@app.route("/upload", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":

        if "file" not in request.files:
            return render_template(
                "upload.html",
                error="No file selected"
            )

        file = request.files["file"]

        if file.filename == "":
            return render_template(
                "upload.html",
                error="Please choose a file"
            )

        if not file.filename.endswith(".py"):
            return render_template(
                "upload.html",
                error="Only Python files are allowed"
            )

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        report = run_bandit_scan(filepath)

        report["scan_time"] = str(datetime.now())
        report["filename"] = file.filename

        report_path = os.path.join(
            REPORT_FOLDER,
            "report.json"
        )

        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

        return redirect(url_for("results"))

    return render_template("upload.html")


@app.route("/results")
def results():

    report_path = os.path.join(
        REPORT_FOLDER,
        "report.json"
    )

    if not os.path.exists(report_path):
        return render_template("results.html", report=None)

    with open(report_path, "r") as f:
        report = json.load(f)

    total, high, medium, low, score = calculate_stats(report)

    return render_template(
        "results.html",
        report=report,
        total=total,
        high=high,
        medium=medium,
        low=low,
        score=score
    )


@app.route("/reports")
def reports():

    report_path = os.path.join(
        REPORT_FOLDER,
        "report.json"
    )

    if os.path.exists(report_path):

        with open(report_path, "r") as f:
            report = json.load(f)

        return render_template(
            "reports.html",
            report=report
        )

    return render_template(
        "reports.html",
        report=None
    )


@app.route("/download-report")
def download_report():

    report_path = os.path.join(
        REPORT_FOLDER,
        "report.json"
    )

    return send_file(
        report_path,
        as_attachment=True
    )


@app.route("/download-pdf")
def download_pdf():

    report_path = os.path.join(
        REPORT_FOLDER,
        "report.json"
    )

    pdf_path = os.path.join(
        REPORT_FOLDER,
        "security_report.pdf"
    )

    if not os.path.exists(report_path):
        return "No report available"

    with open(report_path, "r") as f:
        report = json.load(f)

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Secure Code Auditor Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    filename = Paragraph(
        f"Scanned File: {report.get('filename', '')}",
        styles['BodyText']
    )

    elements.append(filename)

    scan_time = Paragraph(
        f"Scan Time: {report.get('scan_time', '')}",
        styles['BodyText']
    )

    elements.append(scan_time)

    elements.append(Spacer(1, 20))

    if "results" in report:

        for issue in report["results"]:

            issue_text = f"""
            <b>Issue:</b> {issue.get('test_name', '')}<br/>
            <b>Severity:</b> {issue.get('issue_severity', '')}<br/>
            <b>Line:</b> {issue.get('line_number', '')}<br/>
            <b>Description:</b> {issue.get('issue_text', '')}<br/>
            <br/>
            """

            paragraph = Paragraph(
                issue_text,
                styles['BodyText']
            )

            elements.append(paragraph)

            elements.append(Spacer(1, 15))

    doc.build(elements)

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":

    print("Secure Code Auditor Running...")

    app.run(host="127.0.0.1", port=5000)