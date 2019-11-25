from Node import Node
from Search import dfs, dfs_graph, bfs, bfs_graph, iterative_deepening, a_star, a_star_graph
import time


states = []

states.append([[0,0,0,0],[0,'*','A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 1
states.append([[0,0,0,0],['*',0,'A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 2
states.append([['*',0,0,0],[0,0,'A',0],[0,'B',0,0],[0,'C',0,0]]) #depth 3
states.append([[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['*','C',0,0]]) #depth 4
states.append([[0,0,0,0],['A',0,0,0],[0,'B',0,0],[0,'C',0,'*']]) #depth 5
states.append([[0,0,0,0],[0,0,'A',0],[0,'B',0,0],['C',0,'*',0]]) #depth 6
states.append([[0,0,0,0],[0,0,'A',0],['B',0,0,0],[0,'C',0,'*']]) #depth 7
states.append([[0,0,0,0],[0,'A',0,0],[0,'C',0,'B'],[0,0,0,'*']]) #depth 8
states.append([['*',0,0,0],[0,0,'A',0],['B',0,0,0],[0,0,'C',0]]) #depth 9
states.append([[0,0,0,0],[0,'A',0,0],[0,0,0,'B'],['C',0,0,'*']]) #depth 10
states.append([[0,'A',0,0],[0,0,0,0],[0,'B','C',0],[0,0,0,'*']]) #depth 11
states.append([['A',0,0,0],[0,0,0,0],['B',0,0,'*'],[0,0,'C',0]]) #depth 12
states.append([['A',0,0,0],[0,0,0,0],[0,'B','C',0],[0,0,0,'*']]) #depth 13
states.append([[0,0,0,0],[0,0,0,0],[0,0,0,0],['A','B','C','*']]) #depth 14



def find_block(board, block):
        for i in range(len(board)):
            if block in board[i]:
                return i, board[i].index(block)
            else:
                continue


for j in range(len(states)):
    row, column = find_block(states[j],"*")
    node = Node(states[j],row,column,None,None)
    res = a_star_graph(node, "m")
    print(j+1, ",", res[0], ",", res[1], ",", res[2])


for j in range(len(states)):
    row, column = find_block(states[j],"*")
    node = Node(states[j],row,column,None,None)
    res = a_star(node, "m")
    print(j+1, ",", res[0], ",", res[1], ",", res[2])


for i in range(10):
    for j in range(len(states)):
        row, column = find_block(states[j],"*")
        node = Node(states[j],row,column,None,None)
        res = dfs(node)
        print(j+1, ",", res[0], ",", res[1], ",", res[2])


for i in range(10):
    for j in range(len(states)):
        row, column = find_block(states[j],"*")
        node = Node(states[j],row,column,None,None)
        res = dfs_graph(node)
        print(j+1, ",", res[0], ",", res[1], ",", res[2])


for i in range(10):
    for j in range(len(states)):
        row, column = find_block(states[j],"*")
        node = Node(states[j],row,column,None,None)
        res = bfs_graph(node)
        print(j+1, ",", res[0], ",", res[1], ",", res[2])


for i in range(10):
    for j in range(len(states)):
        row, column = find_block(states[j],"*")
        node = Node(states[j],row,column,None,None)
        res = iterative_deepening(node,j+1)
        print(j+1, ",", res[0], ",", res[1], ",", res[2])


for i in range(10):
    for j in range(len(states)):
        row, column = find_block(states[j],"*")
        node = Node(states[j],row,column,None,None)
        res = bfs(node)
        print(j+1, ",", res[0], ",", res[1], ",", res[2])
