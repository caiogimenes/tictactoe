class Node():
    def __init__(self, move, terminal, utility, state, degree):
        self.move = move
        self.terminal = terminal
        self.utility = utility
        self.state = state
        self.degree = degree