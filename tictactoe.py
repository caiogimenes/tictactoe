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
    count_x = 0
    count_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x+=1
            elif board[i][j] == O:
                count_o+=1
    
    return 'X' if count_x <= count_o else 'O'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
        
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_temp = board.deepcopy()
    board_temp[action[0]][action[1]] == player(board)

    return board_temp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """     
    central = board[1][1]
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == central:    
                
    return

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
