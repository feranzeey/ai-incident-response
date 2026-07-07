from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    "flask_requests_total",
    "Total Flask Requests"
)

@app.route("/")
def home():
    REQUESTS.inc()
    return "Application Running"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

app.run(host="0.0.0.0", port=5000)