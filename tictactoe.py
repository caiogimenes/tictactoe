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
    
    best_move = None
    
    def minimizer(board, alpha, beta):
        """
        Returns the minimal value for a state.
        """
        v = float('inf')
        if terminal(board):
            return utility(board)
        for action in actions(board):
            # New state generated from action
            new_board = result(board, action)
            # Update min value found between possible states from action
            v = min(v, maximizer(new_board, alpha, beta))
            # Update the min value found so far for the min player
            beta = min(v, beta)
            # Check if found best so far
            if alpha >= beta:
                break            
                        
        return v
    
    def maximizer(board, alpha, beta):
        """
        Returns the maximal value for a state.
        """
        v = float('-inf')
        if terminal(board):
            return utility(board)
        for action in actions(board):
            # New state generated from action
            new_board = result(board, action)
            # Update max value found between possible states from action
            v = max(v, minimizer(new_board, alpha, beta))
            # Update the max value found so far for the max player
            alpha = max(v, alpha)
            # Check if found best so far
            if alpha >= beta:
                break  
                        
        return v
    
    if player(board) == X:
        max_value = float('-inf')
        for action in actions(board):
            action_eval = minimizer(result(board, action), alpha= float('-inf'), beta= float('inf'))
            if max_value < action_eval:
                max_value = action_eval
                best_move = action
        
        return best_move

    else:
        min_value = float('inf')
        for action in actions(board):
            action_eval = maximizer(result(board, action), alpha= float('-inf'), beta= float('inf'))
            if min_value > action_eval:
                min_value = action_eval
                best_move = action
        
        return best_move