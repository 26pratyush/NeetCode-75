#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

#Example 1: Input: nums = [1, 2, 3, 3]
#Output: true

#Example 2: Input: nums = [1, 2, 3, 4]
#Output: false

#Solution:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(set(nums))<len(nums):
            return True
        else:
            return False

#A set in Python is a data structure that does not allow duplicate values and provides O(1) time complexity
#Converting the list to a set removes duplicates efficiently. 
#If the set's length is less than the original list's length, duplicates existed.
