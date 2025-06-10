class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # The center node must appear in every edge
        # So it must appear in both the first and second edge
        if edges[0][0] == edges[1][0] or edges[0][0] ==  edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]