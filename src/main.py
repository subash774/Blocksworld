from Board import Board

initial_state = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ["A", "B", "C", "*"]
]
goal_state = [
    [0,0,0,0],
    [0,"A",0,0],
    [0,"B",0,0],
    [0,"C",0,"*"]
]
board = Board(initial_state, goal_state)

print(board.state)
print("+"*20)
print(board.move_agent("up"))
print(board.move_agent("up"))
print(board.move_agent("up"))