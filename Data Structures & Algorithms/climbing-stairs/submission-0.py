class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 1
        if n < 0:
            return 0
        
        f = self.climbStairs(n-1)

        s = self.climbStairs(n-2) 

        return f+s