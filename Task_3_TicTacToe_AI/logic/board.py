# board.py
# This file handles board creation and board updates

def create_board():
    """
    Creates and returns an empty Tic-Tac-Toe board
    Board is represented as a list of 9 elements
    """
    return [" " for _ in range(9)]  # 9 empty cells


def make_move(board, index, player):
    """
    Places a player's symbol on the board

    board  -> current board state
    index  -> position (0 to 8)
    player -> "X" or "O"
    """
    # Check if the selected cell is empty
    if board[index] == " ":
        board[index] = player  # Place symbol
        return True             # Move successful
    return False                # Invalid move


def available_moves(board):
    """
    Returns a list of all empty positions
    """
    return [i for i, cell in enumerate(board) if cell == " "]
