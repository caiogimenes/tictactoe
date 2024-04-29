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
    board_temp = board.copy()
    board_temp[action[0]][action[1]] == player(board)

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
    if winner(board):
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
    print("hey")
    if terminal(board):
        return None
    
    turn = player(board)
    moves = actions(board)
    states = []
    
    for move in moves:
        new_board = result(board, move)
        if terminal(new_board):
            util = utility(new_board)
            states.append((move, util))
        states.append((move,utility(result(new_board, minimax(new_board)))))
    
    if turn == 0:
        return min(states, key=lambda x: x[1])[0]
    if turn == X:
        return max(states, key=lambda x: x[1])[0]