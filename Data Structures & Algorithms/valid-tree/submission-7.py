from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        d = defaultdict(list)
        visited = set()

        for i, j in edges:
            if i == j:
                return False
            d[i].append(j)
            d[j].append(i)

        def dfs(par, cur):

            if cur in visited:
                return False
            
            visited.add(cur)

            for child in d[cur]:
                if child == par:
                    continue
                if not dfs(cur, child):
                    return False
            
            return True

        
        return dfs(-1, 0) and len(visited) == n
        