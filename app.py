import os
from flask import Flask, jsonify
from flask_cors import CORS

# Create Flask app
app = Flask(__name__, static_folder="public", static_url_path="")
CORS(app)

# Serve frontend (index.html inside /public)
@app.route("/")
def serve_home():
    return app.send_static_file("index.html")

# API: Get locations
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

# Run server
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
