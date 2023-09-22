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
    countO = 0
    for row in board:
        for element in row:
            if element == X:
                countX+=1
            if element == O:
                countO+=1
    if countX == 0 or countX < countO:
        return X
    
    return O
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
    if not action:
        return board
    
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
        if all(element == row[0] for element in row):
            return row[0]
    # Check diagonal
    diagonal, antidiagonal = set()
    for row in board:
        for i in range(3):
            diagonal.add(row[i][i])
            antidiagonal.add(row[i][2-i]) 
    if len(diagonal) == 1 or len(antidiagonal) == 1 and diagonal[1] is not EMPTY:
        return diagonal[1]
    # Check vertical
    transposed = [[row[i] for row in board] for i in range(3)]
    board = transposed
    for row in board:
        if all(element == row[0] for element in row):
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
    childs = [(result(board, action), action) for action in actions(board)]
    statics = []
    for child in childs:
        if terminal(child):
            statics.append(utility(child))
        else:
            statics.append(utility(result(board, minimax(child))))
    if player(board) == X:        
        max_static = max(statics)
        return childs[childs.index(max_static)][1]
    if player(board) == O:
        min_static = min(statics)
        return childs[childs.index(min_static)][1]