from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)


@app.route("/")
def home():
    REQUEST_COUNT.labels("GET", "/", "200").inc()
    return jsonify({
        "message": "DevOps Capstone CI/CD application is running"
    })


@app.route("/health")
def health():
    REQUEST_COUNT.labels("GET", "/health", "200").inc()
    return jsonify({"status": "healthy"}), 200


@app.route("/ready")
def ready():
    REQUEST_COUNT.labels("GET", "/ready", "200").inc()
    return jsonify({"status": "ready"}), 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


@app.route("/error-test")
def error_test():
    REQUEST_COUNT.labels("GET", "/error-test", "500").inc()
    return jsonify({
        "error": "Intentional error for monitoring test"
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
