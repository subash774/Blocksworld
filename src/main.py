from Node import Node
from Search import dfs, bfs, bfs_graph, iterative_deeping, a_star
initial_state = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ["A", "B", "C", "*"]
]

# initial_state = [[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['*','C',0,0]]



node = Node(initial_state, 3, 3, None, None)
# print(dfs(node, 50))
# bfs(node)
# bfs_graph(node)
# iterative_deeping(node, 4)
print(a_star(node))
