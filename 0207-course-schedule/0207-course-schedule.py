class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict

        # build graph with adjacency list
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u) #v->u (u is prerequist for u)

        visited = set()
        res_stack = set()  # Tracks nodes in current DFS path
        
        def dfs(node):
            if node in res_stack: # Cycle detected
                return False
            
            if node in visited: # Node fully explored
                return True
            
            res_stack.add(node) # Add to recursion stack

            for neighbor in graph[node]:
                if not dfs(neighbor): # Explore neighbors
                    return False

            # After exploring neighbors, remove from rec_stack and mark as visited
            res_stack.remove(node)
            visited.add(node)
            return True

        # Check all nodes to handle disconnected components
        for node in range(numCourses):
            if node not in visited:
                if not dfs(node):
                    return False
        
        return True