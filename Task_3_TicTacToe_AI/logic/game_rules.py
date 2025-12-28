# game_rules.py
# This file checks winning and draw conditions

def check_winner(board, player):
    """
    Checks if the given player has won
    """

    # All possible winning combinations
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),  # Rows
        (0,3,6), (1,4,7), (2,5,8),  # Columns
        (0,4,8), (2,4,6)            # Diagonals
    ]

    # Check each pattern
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True

    return False


def is_draw(board):
    """
    Checks if the game is a draw
    """
    # Draw means no empty space left
    return " " not in board
