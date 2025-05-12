#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.

#Example 1: nums = [3,4,5,6], target = 7
#Output: [0,1] Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

#Example 2: Input: nums = [4,5,6], target = 10
#Output: [0,2]

#Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]

#Tip: Start with two pointers at the beginning and end of the sorted list. Check if A[i][0] + A[j][0] == target.
#If sum is too small, move i forward. If sum is too big, move j backward. If sum matches, return the original indices in sorted order.
