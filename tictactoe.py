"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    if count_x <= count_o:
        return X 
    
    return O

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
    board_temp = deepcopy(board)
    if action:
        board_temp[action[0]][action[1]] = player(board)

    return board_temp

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal and Vertical
    for i in range(3):
        if all(board[i][0]==board[i][j] != EMPTY for j in range(3)):
            return board[i][0]
        if all(board[0][i]==board[j][i] != EMPTY for j in range(3)):
            return board[0][i]
    
    # Diagonal
    if all(board[0][0]==board[i][i] != EMPTY for i in range(3)):
        return board[0][0]
    if all(board[0][2]==board[i][2-i] != EMPTY for i in range(3)):
        return board[0][2]
    
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) or not actions(board):
        return True
    
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    else:
        return 0
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    min_value = float('inf')
    max_value = float('-inf')
    
    turn = player(board)
    
    moves = actions(board)
    best_move = ''
    for move in moves:
        next_board = result(board, move)
        if turn == X:
            if terminal(next_board):
                v = utility(next_board)
            else:
                v = utility(result(next_board, minimax(next_board)))
            if v > max_value:
                max_value = v
                best_move = move
            
        if turn == O:
            if terminal(next_board):
                v = utility(next_board)
            else:
                v = utility(result(next_board, minimax(next_board)))
            if v < min_value:
                min_value = v
                best_move = move
    return best_move            