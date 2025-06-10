class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trust_count = [0] * (n + 1) # How many people trust each person
        trust_others = [0] * (n + 1) # Wether each person trust someone

        for u, v in trust:
            trust_count[v] += 1
            trust_others[u] = True

        for person in range(1, n + 1):
            if trust_count[person] == n - 1 and not trust_others[person]:
                return person

        return -1