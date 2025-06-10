"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned_graph = {}

        def dfs(node):
            # handle null node
            if not node:
                return None

            # handle a node that is already cloned
            if node in cloned_graph:
                return cloned_graph[node]

            # create a new node with the same value
            copy = Node(node.val)

            # store mapping
            cloned_graph[node] = copy

            # recursively clone all the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)
