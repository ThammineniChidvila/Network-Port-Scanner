from flask import Flask, request, jsonify
from flask_cors import CORS
from scanner import scan_target
import os

app = Flask(__name__)
CORS(app)

# Only IP addresses explicitly approved by you can be scanned.
ALLOWED_TARGETS = {
    ip.strip()
    for ip in os.getenv("ALLOWED_TARGETS", "").split(",")
    if ip.strip()
}


@app.route("/")
def home():
    return jsonify({"message": "Network Scanner API is running"})


@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    try:
        target_ip = data.get("ip", "")
        start_port = int(data.get("start_port", 1))
        end_port = int(data.get("end_port", 100))

        result = scan_target(
            target_ip,
            start_port,
            end_port,
            ALLOWED_TARGETS
        )

        return jsonify(result)

    except PermissionError as error:
        return jsonify({"error": str(error)}), 403

    except (ValueError, TypeError):
        return jsonify({"error": "Please enter a valid IP and port range."}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5001)