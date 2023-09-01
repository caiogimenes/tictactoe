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
    for line in board:
        isX = line.count(X)
        isEmpty = line.count(EMPTY)
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
    for i,j in action: 
        if board[i][j]:
        if player(board) == X:
            board[i][j] == X
            return board
        
        board[i][j] == O
        return board
        
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
