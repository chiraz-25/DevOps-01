from flask import Blueprint, jsonify, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/api")
def api():
    return jsonify({
        "name": "Chiraz",
        "role": "DevOps Engineer",
        "skills": ["Docker", "Kubernetes", "AWS", "Terraform"],
        "passion": "Automation & Cloud"
    })

@main.route("/health")
def health():
    return jsonify({"status": "ok"})
