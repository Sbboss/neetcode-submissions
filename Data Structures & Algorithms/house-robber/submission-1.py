class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1]*(len(nums))
        
        def knap(n):
            if n >= len(nums):
                return 0
            
            if dp[n] != -1:
                return dp[n]

            no = knap(n+1)

            yes = knap(n+2) + nums[n]


            dp[n] =  max(yes,no)
            return dp[n]

        return knap(0)