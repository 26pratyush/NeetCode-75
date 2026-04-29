#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

#Example 1: Input: s = "Was it a car or a cat I saw?"
#Output: true
#Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

#Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        s=s.lower()
        s=re.sub('[^a-zA-Z0-9]',"",s)
        print(s)

        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
