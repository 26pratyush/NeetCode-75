#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#Example 1: Input: nums = [1, 2, 3, 3]
#Output: true

#Example 2: Input: nums = [1, 2, 3, 4]
#Output: false

#Solution:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         for i in range(len(nums)):
            dup=0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    dup+=1
            if dup>1:
                return True
         return False

#Tip: Can reduce time complexity by sorting first, then comparing contiguous elements.
