from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
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

        
        for node in range(n):
            if not dfs(node, node):
                return False
            if len(visited) != n:
                return False
        
        return True
        