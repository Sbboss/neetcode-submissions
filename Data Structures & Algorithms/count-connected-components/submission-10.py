class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))
        def find(x):
            if x!= par[x]:
                par[x] = find(par[x])
            
            return par[x]
        
        def union(x,y):
            p1, p2 = find(x), find(y)
            par[p1] = p2
        
        for a,b in edges:
            union(a,b)
        
        res = 0
        vis = set()
        for i in range(n):
            x = find(i)
            if x not in vis:
                res += 1
                vis.add(x)
        
        return res