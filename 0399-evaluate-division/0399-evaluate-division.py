class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1.0 / value))

        def dfs(start: str, end: str, visited: set) -> float:
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, weight in graph[start]:
                if neighbor not in visited:
                    next_result = dfs(neighbor, end, visited)
                    if next_result != -1.0:
                        return weight * next_result
            return -1.0

        result = []
        for c, d in queries:
            result.append(dfs(c, d, set()))

        return result