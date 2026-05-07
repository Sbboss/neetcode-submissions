class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0]*(len(cost)+2)

        for n in range(len(cost)-1, -1, -1):
            dp[n] = min(dp[n+1] + cost[n], dp[n+2] + cost[n])
        

        return min(dp[0], dp[1])

       