class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1]*(len(nums))
        nums[len(nums)-2] = max(nums[-2:])
        
        for i in range(len(nums)-3, -1, -1):
            
            nums[i] = max(nums[i+1], nums[i+2]+nums[i])
        
        return max(nums)