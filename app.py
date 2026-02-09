from flask import Flask, request, jsonify, render_template
from resume_parser import ResumeParser
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    parser = ResumeParser(path)
    result = parser.parse_resume()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
