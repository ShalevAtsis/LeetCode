from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build graph with adjacency list
        graph = defaultdict(list)
        for ai, bi in prerequisites:
            graph[bi].append(ai)  # bi -> ai (bi is prerequisite for ai)

        visited = set()  # Tracks fully explored nodes
        rec_stack = set()  # Tracks nodes in current DFS path
        order = []  # Stores topological order

        def dfs(node):
            if node in rec_stack:  # Cycle detected
                return False
            
            if node in visited:  # Node fully explored
                return True
            
            rec_stack.add(node)  # Add to recursion stack

            for neighbor in graph[node]:
                if not dfs(neighbor):  # Explore neighbors
                    return False

            # After exploring neighbors, remove from rec_stack and mark as visited
            rec_stack.remove(node)
            visited.add(node)
            order.append(node)  # Add to topological order (post-order)
            return True

        # Check all nodes to handle disconnected components
        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return []  # Return empty list if cycle detected
        
        # Reverse the order to get correct topological sort
        return order[::-1]