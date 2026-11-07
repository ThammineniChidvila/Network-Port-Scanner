
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan")
def scan_demo():
    # Safe demonstration using sample scan results
    results = [
        {"port": 21, "service": "FTP", "status": "CLOSED"},
        {"port": 22, "service": "SSH", "status": "OPEN"},
        {"port": 23, "service": "TELNET", "status": "CLOSED"},
        {"port": 80, "service": "HTTP", "status": "OPEN"},
        {"port": 443, "service": "HTTPS", "status": "OPEN"},
    ]

    return jsonify({
        "target": "127.0.0.1 (Demo)",
        "total_scanned": len(results),
        "open_ports": sum(1 for item in results if item["status"] == "OPEN"),
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)
