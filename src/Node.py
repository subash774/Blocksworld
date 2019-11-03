import copy

class Node:

    def __init__(self, board, agent_row, agent_column, parent, path):
        self.board = board
        self.agent_row = agent_row 
        self.agent_column = agent_column
        self.parent = parent
        self.depth =  1 #self.parent.depth + 1
        self.path = path

    def find_block(self, node, block):
        for i in range(len(node)):
            if block in node[i]:
                return i, node[i].index(block)
            else:
                continue
    
    
    def check_goal(self, board):
        return board[1][1] == "A" and board[2][1] == "B" and board[3][1] == "C"

    
    def print_board(self, board):
        for i in range(len(board)):
            print(board[i])
        print("__"*15)


    def check_moves(self, agent_row, agent_column):
        possible = {
            "up" : True,
            "down" : True,
            "left" : True,
            "right" : True
        }
        if agent_row - 1 < 0:
            possible["up"] = False
        if agent_row + 1 > 3:
            possible["down"] = False
        if agent_column - 1 < 0:
            possible["left"] = False
        if agent_column + 1 > 3:
            possible["right"] = False
        
        return possible


    def move_agent(self, new_board, direction):
        agent_row, agent_column = self.find_block(new_board, "*")
        if self.check_moves(agent_row, agent_column).get(direction):
            if direction == "up": 
                # swap the agent with upper block
                new_board[agent_row][agent_column], new_board[agent_row - 1][agent_column] = new_board[agent_row - 1][agent_column], new_board[agent_row][agent_column]
            
            if direction == "down": 
                # swap the agent with lower block
                new_board[agent_row][agent_column], new_board[agent_row + 1][agent_column] = new_board[agent_row + 1][agent_column], new_board[agent_row][agent_column]
        
            if direction == "left": 
                # swap the agent with left block
                new_board[agent_row][agent_column], new_board[agent_row][agent_column -1 ] = new_board[agent_row][agent_column - 1], new_board[agent_row][agent_column]

            if direction == "right": 
                # swap the agent with right block
                new_board[agent_row][agent_column], new_board[agent_row][agent_column + 1 ] = new_board[agent_row][agent_column + 1], new_board[agent_row][agent_column]
            
            agent_row, agent_column = self.find_block(new_board, "*")
            return Node(new_board, agent_row, agent_column, self, direction)
        else:
            return None

        
    def copy(self, board):
        new_board = []
        for item in board:
            new_board.append(item)

        return new_board
    

    def get_children_nodes(self):
        children_nodes = []
        directions = ["up", "left", "right", "down"]
        for direction in directions:
            new_board = copy.deepcopy(self.board)
            new_node = self.move_agent(new_board, direction)
            if new_node is not None:
                children_nodes.append(new_node)
            else:
                continue
        return children_nodes



                


