# Given a string s, return true if it is a palindrome, otherwise return false. A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters. Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1: Input: s = "Was it a car or a cat I saw?"           Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s = re.sub(r'[^a-zA-Z0-9]', '', s)      #remove anything not alphanumeric (whitespaces and &*% )  re.sub(pattern, replacement, string)
        
        s=s.lower()                             #make everything lowercase

        left,right=0,len(s)-1                   #2 pointer approach to verify palindrome
      
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        return True
