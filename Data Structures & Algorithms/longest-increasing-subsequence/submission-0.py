class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def knap(i,j):

            if i == len(nums):
                return 0
            
            res = knap(i+1, j)

            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + knap(i+1, i))

            return res
        
        return knap(0,-1)
