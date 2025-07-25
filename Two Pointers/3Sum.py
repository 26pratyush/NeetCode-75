#Given an integer array nums, return all the triplets 
#[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

#Example 1: Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]

#Solution:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        arr = sorted(nums)
        for i in range(0, len(arr) - 2):  # At least two elements after i
            if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicates for i
                continue
            a, b = i + 1, len(arr) - 1
            while a < b:
                total = arr[a] + arr[b] + arr[i]
                if total == 0:
                    res.append([arr[i], arr[a], arr[b]])
                    while a < b and arr[a] == arr[a + 1]:  # Skip duplicates for a
                        a += 1
                    while a < b and arr[b] == arr[b - 1]:  # Skip duplicates for b
                        b -= 1
                    a += 1
                    b -= 1
                elif total < 0:
                    a += 1
                else:
                    b -= 1
        return res
