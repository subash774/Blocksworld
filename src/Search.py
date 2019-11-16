from Node import Node
from collections import deque

def dfs(start_node, depth):
    fringe_nodes = [start_node] # Stack of nodes
    # fringe_nodes.append(start_node)
    step = 0
    while True:
        if len(fringe_nodes) == 0:
            print("Solution not found")
            return None
        
        node = fringe_nodes.pop()

        if node.check_goal(node.board):
            print("Soluiton found at depth ", node.depth - 1)
            print("Nodes explored: ", step)
            node.print_board(node.board)
            return node

        if node.depth < depth:
            children_nodes = node.get_children_nodes()
            for i in range(len(children_nodes)):
                fringe_nodes.append(children_nodes[i])

        step += 1


def bfs(start_node):
    step = 0
    fringe_nodes = deque([]) # Queue of nodes
    fringe_nodes.append(start_node)

    while True:
        if len(fringe_nodes) == 0:
            print("Soluiton not found")
            return None
        
        node = fringe_nodes.popleft()

        if node.check_goal(node.board):
            print("Solution found at depth ", node.depth)
            return node
        
        for child in node.get_children_nodes():
            fringe_nodes.append(child)
        
        step += 1

def bfs_graph(start_node):
    fringe_nodes = deque([]) # Queue of nodes
    visited_nodes = {}
    fringe_nodes.append(start_node)

    while True:
        if len(fringe_nodes) == 0:
            print("Soluiton not found")
            return None
        
        node = fringe_nodes.popleft()
        visited_nodes[str(node.board)] = 1

        if node.check_goal(node.board):
            print("Solution found at depth ", node.depth)
            node.print_board(node.board)
            return node
        
        for child in node.get_children_nodes():
            if visited_nodes.get(str(child.board)) is None:
                fringe_nodes.append(child)
            

idfs_step = 0
def itd_search(node, depth):
    global idfs_step
    idfs_step += 1
    if node.check_goal(node.board):
            print("Solution found at depth ", node.depth)
            print(f'Nodes expanded: {idfs_step}')
            node.print_board(node.board)
            return node
    
    if depth > 0:
        for child in node.get_children_nodes():
            goal = itd_search(child, depth - 1)
            if goal is not None:
                return goal
            
        return None


def iterative_deeping(start_node, limit):
    for i in range(limit):
        goal = itd_search(start_node, limit)
        if goal is not None:
            break
    return None


