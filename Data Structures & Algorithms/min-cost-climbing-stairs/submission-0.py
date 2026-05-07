class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def knap(n):

            if n >= len(cost):
                return 0
            
            f = knap(n+1) + cost[n]
            s = knap(n+2) + cost[n]

            return min(f,s)
        
        return min(knap(0), knap(1))
        