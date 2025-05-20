#Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
#Each product is guaranteed to fit in a 32-bit integer.

Example 1: Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2: Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = nums.count(0)
        n = len(nums)

        # If more than 1 zero, all outputs are zero
        if zero_count > 1:
            return [0] * n

        # Calculate total product of non-zero elements
        for num in nums:
            if num != 0:
                total_product *= num

        ans = []
        for num in nums:
            if zero_count == 0:
                ans.append(int(total_product / num))
            elif num == 0:
                ans.append(total_product)  # Only 1 zero in input, so this is the position of the zero
            else:
                ans.append(0)  # All other positions become 0
        return ans


#Follow-up: Could you solve it in O(n) time without using the division operation?
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Left pass
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Right pass
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
