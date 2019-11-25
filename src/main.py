from Node import Node
from Search import dfs, bfs, bfs_graph, iterative_deepening, a_star, a_star_graph

import time

initial_state = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ["A", "B", "C", "*"]
]

# initial_state = [[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['*','C',0,0]]
# initial_state = [[0,'A',0,0],
#                 [0,0,0,0],
#                 [0,'B','C',0],
#                 [0,0,0,'*']]

node = Node(initial_state, 3, 3, None, None)
# print(dfs(node))
# bfs(node)
# print(bfs_graph(node))
# print(iterative_deepening(node, 14))
# print(a_star_graph(node, "m"))
# print(a_star(node, "m"))

print(bfs(node))

