from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        d = defaultdict(list)
        visited = set()
        visiting = set()

        def dfs(par, cur):

            if cur in visiting and par != cur:
                return False
            
            if cur in visited:
                return True
            
            if par != cur:
                visiting.add(par)

            for child in d[cur]:
                if not dfs(cur, child) and child != par:
                    return False

            if par in visiting:
                visiting.remove(par)
            visited.add(cur)
            
            return True

        for i, j in edges:
            if i == j:
                return False
            d[i].append(j)
            d[j].append(i)

        
        if not dfs(0, 0):
            return False
        if len(visited) != n:
            return False
        
        return True
        