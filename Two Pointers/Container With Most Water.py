#You are given an integer array heights where heights[i] represents the height of the ith bar.
#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

#Example 1: Input: height = [1,7,2,5,4,7,3,6]
#Output: 36  ( 7 and 6, actual height = smaller ele -> 6. Then width = 7's indice - 6's indice = 7 - 1 = 6. Area = 6 * 6.

#Two pointers: O(n)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        maxw, area = 0,0
        
        while left<right:
            area=(right-left)*min(heights[left],heights[right])
            maxw=max(area, maxw)
            
            if heights[left]>heights[right]:
                right-=1
            elif heights[left]<heights[right]:
                left+=1
            elif heights[left]==heights[right]:
                left+=1
                right-=1
        return maxw
