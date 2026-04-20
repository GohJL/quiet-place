import os 
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder="public", static_url_path="")
CORS(app)

# Serve frontend automatically
@app.route("/")
def serve_home():
    return app.send_static_file("index.html")

# API
@app.route("/api/locations", methods=["GET"])
def get_locations():
    return jsonify([
        {
            "id": 1,
            "name": "UBD Library",
            "location": "library",
            "noise_level": "quiet",
            "crowd_level": "medium",
            "vibe": "silent study"
        }
    ])

# Run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
