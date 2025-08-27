from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)  # allow frontend to talk to backend

# pretend this is our "database"
users = {
    "sato123": "mypassword"
}

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"status": "success", "message": f"Welcome, {username}!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run(debug=True)
