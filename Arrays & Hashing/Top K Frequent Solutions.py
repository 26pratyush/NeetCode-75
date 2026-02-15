#Given an integer array nums and an integer k, return the k most frequent elements within the array.

#Example 1: Input: nums = [1,2,2,3,3,3], k = 2
#Output: [2,3]

#Example 2: Input: nums = [7,7], k = 1
#Output: [7]

#Solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}                                    #create hashmap
        for num in nums:
            freq[num] = freq.get(num, 0) + 1       #record frequency of each element

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)    #sort hashmap in descending order (most frequent)

        res=[]
        for i in range(k):
            res.append(sorted_freq[i][0])        #append k number of elements
        return res
