"""
Tic Tac Toe Player
"""

from copy import deepcopy
from utils import Node

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
    for row in board:
        for element in row:
            if element == X:
                count_x+=1
            if element == O:
                count_o+=1
    if count_x == 0 or count_x <= count_o:
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
    new_board = deepcopy(board)
    if not action:
        return new_board
    if player(board) == X:
        new_board[action[0]][action[1]] = X
        return new_board
    elif player(board) == O:
        new_board[action[0]][action[1]] = O
        return new_board   


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizonal
    for row in board:
        if all(element == row[0] for element in row):
            return row[0]
    # Check diagonal
    diagonal = []
    antidiagonal = []
    for i in range(3):
        diagonal.append(board[i][i])
        antidiagonal.append(board[i][2-i])
    if all(element == diagonal[0] for element in diagonal):
        return diagonal[0]
    if all(element == antidiagonal[0] for element in antidiagonal):
        return antidiagonal[0]
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
    if winner(board) or len(actions(board)) == 0:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    results = winner(board)
    if results == O:
        return -1
    if results == X:
        return 1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    """
    THE OPTIMAL WAY IS THE ONE THAT HAS THE SHORTER LENGHT TO VICTORY!!!!!!!
    """
    if terminal(board):
        return None
    
    moves = actions(board) 
    
    if player(board) == X:
        max_value = float('-inf')
        max_move = None
        for move in moves:
            state = result(board, move)
            if terminal(state):
                score = utility(state)
                if utility(state) > max_value:
                    max_value = score
                    max_move = move
        return max_move
    
    if player(board) == O:
        min_value = float('inf')
        min_move = None
        for move in moves:
            state = result(board, move)
            if terminal(state):
                score = utility(state)
                if utility(state) > min_value:
                    min_value = score
                    min_move = move
        return min_move