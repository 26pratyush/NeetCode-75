# You are given an array of length n which was originally sorted in ascending order. 
# It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:
# [3,4,5,6,1,2] if it was rotated 4 times.
# Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.
# A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

# Example 1: Input: nums = [3,4,5,6,1,2]
# Output: 1'''

#Solution:
def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[right]:
            right = mid                # min is in left half (including mid)
        else:
            left = mid + 1             # min is in right half

    return nums[left]                  # can also return nums[right] as both point to the pivot / smallest element
