class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [-1]*(len(cost)+1)

        def knap(n):

            if n >= len(cost):
                return 0
            
            if dp[n] != -1:
                return dp[n]

            f = knap(n+1) + cost[n]
            s = knap(n+2) + cost[n]

            dp[n] = min(f,s)

            return dp[n]
        knap(0)
        return min(dp[0], dp[1])
        