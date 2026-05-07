class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numset = set(nums)

         return True if len(nums) != len(numset) else False