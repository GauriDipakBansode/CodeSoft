from flask import Flask, render_template, request, jsonify
from chatbot import detect_concept, get_response


# create Flask app
app = Flask(__name__)

# This is simple test route
@app.route("/")

def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_input = request.json.get("message")

    concept = detect_concept(user_input)

    response = get_response(concept)


    return jsonify({"reply": response})

#Start the server
if __name__ == "__main__":
    app.run(debug=True)


