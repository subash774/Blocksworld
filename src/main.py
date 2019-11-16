from Node import Node
from Search import dfs, bfs, bfs_graph, iterative_deeping
initial_state = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ["A", "B", "C", "*"]
]



node = Node(initial_state, 3, 3, None, None)
# dfs(node, 14)
# bfs(node)
# bfs_graph(node)
iterative_deeping(node, 100)