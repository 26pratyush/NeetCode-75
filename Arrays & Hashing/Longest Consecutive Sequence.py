#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
#The elements do not have to be consecutive in the original array.
#You must write an algorithm that runs in O(n) time.

#Example 1: Input: nums = [2,20,4,10,3,4,5]
#Output: 4

#Solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))  # remove duplicates and sort
        longest = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
                longest = max(longest, current_streak)
            else:
                current_streak = 1
        return longest


#Tip: O(n) Solution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        return res
