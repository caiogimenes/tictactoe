
class Node():
    def __init__(self, move, state):
        self.move = move
        self.state = state

class Path():
    def __init__(self):
        self.path = []
        self.utility = []
    
    def add_node(self, node):
        self.path.append(node)
    
    def remove_node(self, node):
        self.path.remove(node)
    
    def end_node(self):
        return self.path[len(self.path) - 1]
    
    def degree(self):
        return len(self.path)