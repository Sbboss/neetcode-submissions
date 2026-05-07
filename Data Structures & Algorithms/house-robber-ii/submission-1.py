class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def knap(num):
            r1,r2 = 0,0

            for i in num:
                tmp = max(i+r1, r2)
                r1 = r2
                r2 = tmp
            
            return r2
        
        return max(knap(nums[1:]), knap(nums[:-1])) if len(nums) > 1 else nums[0]