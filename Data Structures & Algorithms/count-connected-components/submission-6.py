class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        d = defaultdict(list)
        visited = set()

        for i, j in edges:
            d[i].append(j)
            d[j].append(i)

        def dfs(cur):

            if cur in visited:
                return True
            
            visited.add(cur)

            for child in d[cur]:
                if not dfs(child):
                    return False
            
            return True

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
            if len(visited) == n:
                return res

        # return res
        