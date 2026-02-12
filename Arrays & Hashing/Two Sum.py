#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.

#Example 1: nums = [3,4,5,6], target = 7
#Output: [0,1] Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

#Solution: Crude approach when list is already sorted:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                return left,right
            elif nums[left]+nums[right]<target:
                left+=1
            elif nums[left]+nums[right]>target:
                right-=1

#Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        # Go through each number in the list along with its index
        for i in range(len(nums)):
            num = nums[i]  # Current number
            inverse = target - num  # The number we need to find a pair

            # Check if the matching number is already in the dictionary
            if inverse in seen:
                return [seen[inverse], i]    # If it is, we found the pair that adds up to the target

            seen[num] = i     # Otherwise, store this number and its index in the dictionary
            
'''This solution uses a hash map (seen dictionary) to find two numbers that sum to the target. 
It iterates through the array, for each number, calculates the complement needed to reach the target. 
If the complement is already in seen (meaning it was encountered earlier), 
it returns the stored index of the complement and the current number's index. 
Otherwise, it adds the current number and its index to seen for future checks.'''

#Tip: You can also use 2 pointers but worse time C. Start with two pointers at the beginning and end of the sorted list. Check if A[i][0] + A[j][0] == target.
#If sum is too small, move i forward. If sum is too big, move j backward. If sum matches, return the original indices in sorted order.
