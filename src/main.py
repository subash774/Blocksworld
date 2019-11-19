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
# dfs(node, 50)
# bfs(node)
# bfs_graph(node)
# iterative_deeping(node, 4)
a_star(node)
# states = []
# states.append([[0,0,0,0],[0,0,0,0],[0,0,0,0],['A','B','C','*']]) #depth 14
# states.append([['A',0,0,0],[0,0,0,0],[0,'B','C',0],[0,0,0,'*']]) #depth 13
# states.append([['A',0,0,0],[0,0,0,0],['B',0,0,0],[0,0,'C','*']]) #depth 12
# states.append([[0,'A',0,0],[0,0,0,0],[0,'B','C',0],[0,0,0,'*']]) #depth 11
# states.append([[0,0,0,0],[0,'A',0,0],[0,0,0,'B'],['C',0,0,'*']]) #depth 10
# states.append([['*',0,0,0],[0,0,'A',0],['B',0,0,0],[0,0,'C',0]]) #depth 9
# states.append([[0,0,0,0],[0,'A',0,0],[0,'C',0,'B'],[0,0,0,'*']]) #depth 8
# states.append([[0,0,0,0],[0,0,'A',0],['B',0,0,0],[0,'C',0,'*']]) #depth 7
# states.append([[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['C',0,'*',0]]) #depth 6
# states.append([[0,0,0,0],['A',0,0,0],[0,'B',0,0],[0,'C',0,'*']]) #depth 5
# states.append([[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['*','C',0,0]]) #depth 4
# states.append([['*',0,0,0],[0,0,'A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 3
# states.append([[0,0,0,0],['*',0,'A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 2
# states.append([[0,0,0,0],[0,'*','A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 1