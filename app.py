from flask import Flask, render_template, request, jsonify
from wabai import generate_response
from config.settings import Config

# Validate configuration
Config.validate()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            response = generate_response(user_input)
    return render_template("index.html", response=response)

@app.route("/api/chat", methods=["POST"])
def api_chat():
    """API endpoint for chat (for future use)"""
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400
    
    user_input = data["message"].strip()
    if not user_input:
        return jsonify({"error": "Message cannot be empty"}), 400
    
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(
        debug=Config.FLASK_DEBUG,
        port=Config.FLASK_PORT,
        host=Config.FLASK_HOST
    )

