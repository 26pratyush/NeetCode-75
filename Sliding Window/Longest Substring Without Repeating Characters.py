# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Example 1: Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for left in range(n):
            for right in range(left, n):
                substring = s[left:right+1]

                if len(set(substring)) == len(substring):
                    ans = max(ans, right - left + 1)
        return ans
