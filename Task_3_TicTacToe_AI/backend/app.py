# app.py
# Flask backend for Tic-Tac-Toe AI

import sys
import os

# Allows backend to access logic folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify, render_template

# Import logic modules
from logic.board import create_board, make_move
from logic.game_rules import check_winner, is_draw
from logic.ai_player import get_best_move

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# -----------------------------
# GAME STATE (GLOBAL)
# -----------------------------
# Board is shared between moves
board = create_board()
game_over = False 
# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    """
    Serves the game UI
    """
    return render_template("index.html")

# -----------------------------
# MOVE API
# -----------------------------
@app.route("/move", methods=["POST"])
def play_move():
    """
    Receives human move, returns AI move
    """

    global board, game_over

    if game_over:
        return jsonify({
            "board": board,
            "result": "Game Over"
        })

    data = request.get_json()
    human_move = data.get("move")

    # Human plays
    if not make_move(board, human_move, "X"):
        return jsonify({"error": "Invalid move"})

    if check_winner(board, "X"):
        game_over = True
        return jsonify({"board": board, "result": "Human Wins!"})

    if is_draw(board):
        game_over = True
        return jsonify({"board": board, "result": "Draw!"})


    # AI plays
    ai_move = get_best_move(board)
    make_move(board, ai_move, "O")

    # Check AI win
    # Check draw again
    if check_winner(board, "O"):
        game_over = True
        return jsonify({"board": board, "result": "AI Wins!"})

    if is_draw(board):
        game_over = True
        return jsonify({"board": board, "result": "Draw!"})


    # Normal game response
    return jsonify({
        "board": board,
        "ai_move": ai_move,
        "result": "Continue"
    })

# -----------------------------
# RESET GAME
# -----------------------------
@app.route("/reset", methods=["POST"])
def reset_game():
    global board, game_over
    board = create_board()
    game_over = False
    return jsonify({"board": board})

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
