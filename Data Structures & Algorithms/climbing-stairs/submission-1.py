class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [-1]*(n+1)

        def knap(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            f = self.climbStairs(n-1)

            s = self.climbStairs(n-2) 

            dp[n] = f+s

            return dp[n]
        
        return knap(n)