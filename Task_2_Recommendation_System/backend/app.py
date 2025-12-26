import sys
import os

# Make sure logic folder is accessible
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, render_template, jsonify
from logic.data_loader import load_data, create_user_item_matrix
from logic.similarity import compute_similarity
from logic.recommender import recommend_products

# -----------------------------
# FLASK APP INITIALIZATION
# -----------------------------
app = Flask(__name__)  # templates -> templates/, static -> static/ by default

# -----------------------------
# DATA LOADING
# -----------------------------
DATA_PATH = "../data/ratings.csv"

# Load CSV and clean data
df = load_data(DATA_PATH)

# Create user-item matrix (rows=users, columns=products, values=ratings)
user_item_matrix = create_user_item_matrix(df)

# -----------------------------
# FIX: Ensure index is integer
# -----------------------------
user_item_matrix.index = user_item_matrix.index.astype(int)

# Compute similarity between users
similarity_matrix = compute_similarity(user_item_matrix)

# -----------------------------
# HOME ROUTE (FRONTEND)
# -----------------------------
@app.route("/")
def home():
    """
    Render the main page.
    """
    return render_template("index.html")


# -----------------------------
# RECOMMENDATION API
# -----------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    """
    API endpoint to get top-N recommendations for a user.
    Expects JSON: {"user_id": 1}
    Returns JSON: {"user_id": 1, "recommendations": [...]}
    """
    data = request.get_json()
    user_id = data.get("user_id")

    # Convert user_id to int
    try:
        user_id = int(user_id)
    except (ValueError, TypeError):
        return jsonify({
            "user_id": user_id,
            "recommendations": [],
            "message": "Invalid user ID."
        }), 400

    # Check if user exists
    if user_id not in user_item_matrix.index:
        return jsonify({
            "user_id": user_id,
            "recommendations": [],
            "message": "User not found."
        }), 404

    # Get recommendations
    recommendations = recommend_products(
        user_id,
        user_item_matrix,
        similarity_matrix,
        top_n=5
    )

    return jsonify({
        "user_id": user_id,
        "recommendations": recommendations
    })


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
