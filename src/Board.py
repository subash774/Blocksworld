class Board:
    state = None
     
    @classmethod
    def update_state(cls, state):
        cls.state = state

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.size = len(initial_state)

        self.update_state(initial_state)

    def check_goal(self, board):
        return board[1][1] == "A" and board[2][1] == "B" and board[3][1] == "C"
    

    def find_block(self, block):
        for i in range(len(self.initial_state)):
            if block in self.initial_state[i]:
                return i, self.initial_state[i].index(block)
            else:
                continue

    
    def check_moves(self, agent_row, agent_column):
        print(agent_row, agent_column)
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


    def move_agent(self, direction):
        agent_row, agent_column = self.find_block("*")
        new_state = self.state.copy()
        if self.check_moves(agent_row, agent_column).get(direction):
            if direction == "up": 
                # swap the agent with another block
                new_state[agent_row][agent_column], new_state[agent_row - 1][agent_column] = new_state[agent_row - 1][agent_column], new_state[agent_row][agent_column]
            
            if direction == "down": 
                # swap the agent with another block
                new_state[agent_row][agent_column], new_state[agent_row + 1][agent_column] = new_state[agent_row + 1][agent_column], new_state[agent_row][agent_column]
        
            if direction == "left": 
                # swap the agent with another block
                new_state[agent_row][agent_column], new_state[agent_row][agent_column -1 ] = new_state[agent_row][agent_column - 1], new_state[agent_row][agent_column]

            if direction == "right": 
                # swap the agent with another block
                new_state[agent_row][agent_column], new_state[agent_row][agent_column + 1 ] = new_state[agent_row][agent_column + 1], new_state[agent_row][agent_column]

        
        return new_state
        
    
                


