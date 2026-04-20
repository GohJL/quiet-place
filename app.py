import os 
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="public", static_url_path="")
CORS(app)


# Sample data (replace with database later)
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

@app.route("/home")
def home():
    return "Hello"
    
# Serve frontend
@app.route("/")
def serve_home():
    return send_from_directory("public", "index.html")

# GET locations
@app.route("/api/locations", methods=["GET"])
def get_locations():
    return jsonify(locations)

# POST update
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
