import copy
import random

class Node:

    def __init__(self, board, agent_row, agent_column, parent, path):
        self.board = board
        self.agent_row = agent_row 
        self.agent_column = agent_column
        self.parent = parent
        if parent is not None: 
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
        self.path = path


    def __hash__(self):
        return hash(str(self.board))
    

    def __eq__(self, other):
        return str(self.board) == str(other.board)


    def find_block(self, board, block):
        for i in range(len(board)):
            if block in board[i]:
                return i, board[i].index(block)
            else:
                continue
    
    
    def check_goal(self, board):
        return board[3][1] == "C" and board[2][1] == "B" and board[1][1] == "A"

    
    def print_board(self, board):
        print("-----------------")
        for i in board:
            vertical_dash = "| "
            for j in i:
                vertical_dash = vertical_dash + str(j) + " | "
            print(vertical_dash)
            print("-----------------")

     

    def check_moves(self, agent_row, agent_column, board):
        possible = {
            "up" : True,
            "down" : True,
            "left" : True,
            "right" : True
        }
        if agent_row - 1 < 0 or board[agent_row][agent_column] == "X":
            possible["up"] = False
        if agent_row + 1 > 3 or board[agent_row][agent_column] == "X":
            possible["down"] = False
        if agent_column - 1 < 0 or board[agent_row][agent_column] == "X":
            possible["left"] = False
        if agent_column + 1 > 3 or board[agent_row][agent_column] == "X":
            possible["right"] = False
        
        return possible


    def move_agent(self, new_board, direction):
        agent_row, agent_column = self.find_block(new_board, "*")
        if self.check_moves(agent_row, agent_column, new_board).get(direction):
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
        random.shuffle(children_nodes)
        return children_nodes
    

    def get_man_heuristic(self):
        a = self.find_block(self.board, "A")
        b = self.find_block(self.board, "B")
        c = self.find_block(self.board, "C")



        man_dist = (abs(a[0] - 1) + abs(a[1] - 1)
                    + abs(b[0] - 2) + abs(b[1] - 1)
                    + abs(c[0] - 3) + abs(c[1] - 1))
        
        return man_dist
        
    
    def get_cheb_heuristic(self):
        a = self.find_block(self.board, "A")
        b = self.find_block(self.board, "B")
        c = self.find_block(self.board, "C")

        cheb_dist = (max(abs(a[1] - b[1]),
                    abs(b[1] - c[1]),
                    abs(a[1] - c[1])) 
                    * 
                    max(abs(a[0] - b[0]),
                    abs(b[0] - c[0]),
                    abs(a[0] - c[0])))
        
        return (cheb_dist + self.get_man_heuristic())/2