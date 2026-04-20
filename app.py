import os 
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder="public")
CORS(app)

# Sample data
locations = [
    {
        "id": 1,
        "name": "UBD Library",
        "location": "library",
        "noise_level": "quiet",
        "crowd_level": "medium",
        "vibe": "silent study"
    },
    {
        "id": 2,
        "name": "Campus Cafe",
        "location": "cafe",
        "noise_level": "moderate",
        "crowd_level": "high",
        "vibe": "relaxed"
    }
]

# Serve frontend
@app.route("/")
def serve_home():
    return app.send_static_file("index.html")

# API routes
@app.route("/api/locations", methods=["GET"])
def get_locations():
    return jsonify(locations)

@app.route("/api/update", methods=["POST"])
def update_location():
    data = request.json
    loc_id = data.get("id")

    for loc in locations:
        if loc["id"] == loc_id:
            loc["noise_level"] = data.get("noise_level")
            loc["crowd_level"] = data.get("crowd_level")
            return jsonify({"message": "Updated", "data": loc})

    return jsonify({"error": "Location not found"}), 404

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
