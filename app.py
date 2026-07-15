from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/health")
def health():
    return jsonify(status="ok")

@app.get("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Kyle"},
        {"id": 2, "name": "Marta"},
    ])

@app.post("/webhook")
def webhook():
    data = request.get_json(silent=True)
    if not data:
        return jsonify(error="No JSON received"), 400

    print("Webhook received:", data)
    return jsonify(received=True, data=data), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
