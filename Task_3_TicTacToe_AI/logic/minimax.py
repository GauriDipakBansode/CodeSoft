# minimax.py
# This file implements the Minimax algorithm

from logic.game_rules import check_winner, is_draw
from logic.board import available_moves


def minimax(board, depth, is_maximizing):
    """
    Minimax algorithm implementation

    board          -> current game board
    depth          -> recursion depth
    is_maximizing  -> True for AI, False for Human
    """

    # Base conditions (game over)
    if check_winner(board, "O"):   # AI wins
        return 1
    if check_winner(board, "X"):   # Human wins
        return -1
    if is_draw(board):             # Draw
        return 0

    # AI turn (maximize score)
    if is_maximizing:
        best_score = -float("inf")

        for move in available_moves(board):
            board[move] = "O"                       # Try move
            score = minimax(board, depth+1, False) # Recursive call
            board[move] = " "                       # Undo move
            best_score = max(score, best_score)

        return best_score

    # Human turn (minimize score)
    else:
        best_score = float("inf")

        for move in available_moves(board):
            board[move] = "X"
            score = minimax(board, depth+1, True)
            board[move] = " "
            best_score = min(score, best_score)

        return best_score
