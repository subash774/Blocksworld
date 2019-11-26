from Node import Node
from collections import deque
from queue import PriorityQueue as Q
import time

def dfs(start_node):
    fringe_nodes = [start_node] # Stack of nodes
    nodes_expanded = 0
    while True:
        if len(fringe_nodes) == 0:
            print("Solution not found")
            return None
        
        node = fringe_nodes.pop()

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return ["DFS", node.depth, nodes_expanded]


        children_nodes = node.get_children_nodes()
        for child in children_nodes:
            fringe_nodes.append(child)

        nodes_expanded += 1


def dfs_graph(start_node):
    fringe_nodes = [start_node] # Stack of nodes
    nodes_expanded = 0
    visited_nodes = {}

    while True:
        if len(fringe_nodes) == 0:
            print("Solution not found")
            return None
        
        node = fringe_nodes.pop()

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return ["DFS Graph", node.depth, nodes_expanded]


        children_nodes = node.get_children_nodes()
        for child in children_nodes:
            if visited_nodes.get(str(child.board)) is None:
                fringe_nodes.append(child)

        nodes_expanded += 1

def bfs(start_node):
    nodes_expanded = 0
    fringe_nodes = deque([]) # Queue of nodes
    fringe_nodes.append(start_node)
    t_end = time.time() + 60 * 15 # 15 min time limit
    while True:
        if time.time() < t_end:
            if len(fringe_nodes) == 0:
                print("Solution not found")
                return None
            
            node = fringe_nodes.popleft()

            if node.check_goal(node.board):
                # Search name, depth, nodes expanded
                return ["BFS", node.depth, nodes_expanded]
            
            for child in node.get_children_nodes():
                fringe_nodes.append(child)
            
            nodes_expanded += 1
        else:
            return None


def bfs_graph(start_node):
    fringe_nodes = deque([]) # Queue of nodes
    visited_nodes = {}
    fringe_nodes.append(start_node)
    nodes_expanded = 0

    while True:
        if len(fringe_nodes) == 0:
            print("Solution not found")
            return None
        
        node = fringe_nodes.popleft()
        visited_nodes[str(node.board)] = 1

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return ["BFS_Graph", node.depth, nodes_expanded]
        
        for child in node.get_children_nodes():
            if visited_nodes.get(str(child.board)) is None:
                fringe_nodes.append(child)
        
        nodes_expanded += 1


def depth_limited(start_node, depth):
    fringe_nodes = [start_node] # Stack of nodes
    nodes_expanded = 0

    if len(fringe_nodes) == 0:
        print("Solution not found")
        return None
        
    while len(fringe_nodes) > 0:
        
        node = fringe_nodes.pop()

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            return node, nodes_expanded, True

        if node.depth < depth:
            children_nodes = node.get_children_nodes()
            for child in children_nodes:
                fringe_nodes.append(child)

            nodes_expanded += 1


def iterative_deepening(start_node, limit):
    for i in range(limit):
        node, nodes_expanded, goal = depth_limited(start_node, limit)
        if goal:
            break
    return ["IDS", node.depth, nodes_expanded]
    

def a_star_graph(start_node, h):
    visited_nodes = {}
    fringe_nodes = Q()
    nodes_expanded = 0

    fringe_nodes.put((start_node.get_man_heuristic(), start_node))

    if fringe_nodes.qsize() == 0:
        print("Solution not found")
        return None
    
    while fringe_nodes.qsize()  > 0:
    # for i in range(5):
        node = fringe_nodes.get()[1]
        # node.print_board(node.board)
        visited_nodes[str(node.board)] = 1
        
        # node.print_board(node.board)

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            # node.print_board(node.board)
            return ["A* Graph", node.depth, nodes_expanded]
        
        
        children = node.get_children_nodes()
        nodes_expanded += 1

        for child in children:
            if visited_nodes.get(str(child.board)) is not None:
                continue
            if h == "m":
                fringe_nodes.put((child.depth + child.get_man_heuristic(), child))
            if h == "c":
                fringe_nodes.put((child.depth + child.get_cheb_heuristic(), child))
    

def a_star(start_node, h):
    fringe_nodes = Q()
    nodes_expanded = 0
    fringe_nodes.put((start_node.get_man_heuristic(), start_node))

    if fringe_nodes.qsize() == 0:
        print("Solution not found")
        return None
    
    while fringe_nodes.qsize() > 0:
    # for i in range(5):
        node = fringe_nodes.get()[1]

        if node.check_goal(node.board):
            # Search name, depth, nodes expanded
            # node.print_board(node.board)
            return ["A*", node.depth, nodes_expanded]
    
        
        children = node.get_children_nodes()
        nodes_expanded += 1

        for child in children:
            if h == "m":
                fringe_nodes.put((child.depth + child.get_man_heuristic(), child))
            if h == "c":
                fringe_nodes.put((child.depth + child.get_cheb_heuristic(), child))
   
