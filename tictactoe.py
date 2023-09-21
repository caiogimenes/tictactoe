"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countEmpty = 0    
    for row in board:
        isX = row.count(X)
        isEmpty = row.count(EMPTY)
        countX += isX
        countEmpty += isEmpty
    
    if countEmpty == 0:
        return None
    
    if countX % 2 == 0:
        return O
    
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allowed = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                allowed.append((i,j))
                
    return allowed


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]
    if board[i][j] == EMPTY: 
        if player(board) == X:
            board[i][j] = X
            return board
        else:
            board[i][j] = O
            return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizonal
    for row in board:
        # Convert to a set and check if only returns one element
        if len(set(row)) == 1:
            return row[0]
    # Check diagonals
    diagonals = [board[i][i] for i in range(3)]
    diagonals.append([board[i][2-i] for i in range(3)])
    for diagonal in diagonals:
        if diagonal and len(set(diagonal)) == 1:
            return diagonal[0]
    # Check vertical
    # Transpose the collumns to the rows
    transposed = [[board[j][i] for j in range(3)] for i in range(3)]
    board = transposed  
    for row in board:
        # Convert to a set and check if only returns one element
        if len(set(row)) == 1:
            return row[0]     

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not player(board):
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == O:
        return -1
    if result == X:
        return 1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    