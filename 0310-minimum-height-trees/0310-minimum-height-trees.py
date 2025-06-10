class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        from collections import defaultdict, deque
        graph = defaultdict(list)
        degrees = [0] * n

        for ai, bi in edges:
            graph[ai].append(bi)
            graph[bi].append(ai)
            degrees[ai] += 1
            degrees[bi] += 1

        queue = deque([i for i in range(n) if degrees[i] == 1])
        remaining_nodes = n

        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size
            for _ in range(size):
                leaf = queue.popleft()
                for neighbor in graph[leaf]:
                    degrees[neighbor] -= 1
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue) if remaining_nodes > 0 else []