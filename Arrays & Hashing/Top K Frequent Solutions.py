#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#The test cases are generated such that the answer is always unique.
#You may return the output in any order.

#Example 1: Input: nums = [1,2,2,3,3,3], k = 2
#Output: [2,3]

#Example 2: Input: nums = [7,7], k = 1
#Output: [7]

#Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number using a dictionary
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1  # Increment the count if the number already exists
            else:
                freq_map[num] = 1   # Otherwise, add the number with count 1

        # Step 2: Sort the items in the frequency map by frequency in descending order
        # freq_map.items() gives (number, frequency) pairs
        # key=lambda item: item[1] means we're sorting by the frequency value
        # reverse=True puts the most frequent items first
        sorted_items = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)

        # Step 3: Collect the top k elements (most frequent numbers)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])  # Only take the number, not its frequency

        # Step 4: Return the list of top k frequent elements
        return result
