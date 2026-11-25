
from flask import Flask, render_template, request, jsonify

from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_bot_response():

    data = request.get_json(silent=True) or {}

    user_message = data.get("msg", "")

    if not isinstance(user_message, str) or not user_message.strip():

        return jsonify({
            "response": "Please enter a valid message."
        }), 400

    response = get_response(user_message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":

    app.run(debug=True)
