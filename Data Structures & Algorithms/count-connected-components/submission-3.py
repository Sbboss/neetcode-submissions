class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if len(edges) > n - 1:
        #     return False

        d = defaultdict(list)
        visited = set()

        for i, j in edges:
            # if i == j:
            #     return False
            d[i].append(j)
            d[j].append(i)

        def dfs(par, cur):

            if cur in visited:
                return True
            
            visited.add(cur)

            for child in d[cur]:
                if child == par:
                    continue
                if not dfs(cur, child):
                    return False
            
            return True

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i,i)
            print(visited)
            if len(visited) == n:
                print(res)
                return res

        return res
        