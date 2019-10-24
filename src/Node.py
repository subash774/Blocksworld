class Node:
    def __init__(self, current_state, parent, depth, path):
        self.current_state = current_state
        self.parent = parent
        self.depth = depth
        self.path = path
    
    def find_block(self):
        for i in range(len(self.current_state)):
            if block in self.current_state[i]:
                return [i, self.current_state[i].index(block)]
            else:
                continue