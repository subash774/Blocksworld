from Node import Node
from collections import deque

def dfs(start_node, depth):
    fringe_nodes = [start_node] # Stack of nodes
    step = 0
    while True:
        if len(fringe_nodes) == 0:
            print("Solution not found")
            return None
        
        node = fringe_nodes.pop()

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return ["DFS", node.depth, step]

        if node.depth < depth:
            children_nodes = node.get_children_nodes()
            for child in children_nodes:
                fringe_nodes.append(child)

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
            # Search name, depth, nodes expanded
            return ["BFS", node.depth, step]
        
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
            # Search name, depth, nodes expanded
            return ["BFS_Graph", node.depth, step]
        
        for child in node.get_children_nodes():
            if visited_nodes.get(str(child.board)) is None:
                fringe_nodes.append(child)
            

idfs_step = 0
def itd_search(node, depth):
    global idfs_step
    idfs_step += 1
    if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return ["IDFS", node.depth, step]
    
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


def a_star(start_node):
    visited_nodes = {}
    fringe_nodes = [start_node]
    step = 0

    if len(fringe_nodes) == 0:
            print("Soluiton not found")
            return None
    
    while len(fringe_nodes) > 0:
        node = fringe_nodes.pop()
        visited_nodes[str(node.board)] = 1

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            node.print_board(node.board)
            return ["A*", node.depth, step]
        
        
        children = node.get_children_nodes()
        step += 1

        for child in children:
            if visited_nodes.get(str(child.board)) is not None:
                continue

            fringe_nodes.append(child)

        fringe_nodes.sort(key=lambda x: x.depth + x.get_man_heuristic(), reverse = True)
    





