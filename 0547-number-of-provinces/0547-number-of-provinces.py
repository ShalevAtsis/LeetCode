class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(isConnected)

        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)
        
        def dfs(node: int, visited = set):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
        
        visited = set()
        components = 0
        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                components += 1

        return components