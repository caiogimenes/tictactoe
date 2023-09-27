class Node():
    def __init__(self, move, state):
        self.move = move
        self.state = state

class Path():
    def __init__(self):
        self.nodes = []
        self.utility = None
    
    def add_node(self, node):
        self.nodes.append(node)
        
    def end_node(self):
        return self.nodes[len(self.nodes) - 1]
    
    def degree(self):
        return len(self.nodes)