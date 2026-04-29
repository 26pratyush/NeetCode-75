# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Example 1: Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
            
        for i in range(len(s)):
            chars=set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                        
                else:
                    chars.add(s[j])
                    maxl=max(maxl,len(chars))
        return maxl
