# ai_player.py
# This file decides the best move for AI

from logic.minimax import minimax
from logic.board import available_moves


def get_best_move(board):
    """
    Returns the best move index for AI
    """

    best_score = -float("inf")
    best_move = None

    # Try all possible moves
    for move in available_moves(board):
        board[move] = "O"                     # AI makes move
        score = minimax(board, 0, False)      # Evaluate
        board[move] = " "                     # Undo move

        if score > best_score:
            best_score = score
            best_move = move

    return best_move
