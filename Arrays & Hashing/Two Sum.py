#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.

#Example 1: nums = [3,4,5,6], target = 7
#Output: [0,1] Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

#Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}
        for i, num in enumerate(nums):
            inverse=target-num
            if inverse in seen:
                return [seen[inverse],i]
            seen[num]=i
            
'''This solution uses a hash map (seen dictionary) to find two numbers that sum to the target. 
It iterates through the array, for each number, calculates the complement needed to reach the target. 
If the complement is already in seen (meaning it was encountered earlier), 
it returns the stored index of the complement and the current number's index. 
Otherwise, it adds the current number and its index to seen for future checks.'''

#Tip: You can also use 2 pointers but worse time C. Start with two pointers at the beginning and end of the sorted list. Check if A[i][0] + A[j][0] == target.
#If sum is too small, move i forward. If sum is too big, move j backward. If sum matches, return the original indices in sorted order.
