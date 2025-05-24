#Given a string s, return true if it is a palindrome, otherwise return false.
#A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

#Example 1: Input: s = "Was it a car or a cat I saw?"
#Output: true
#Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

#Solution:
class Solution:
    def isPalindrome(self, x: str) -> bool:
        s = x.lower()
        s = ''.join(c for c in s if c.isalnum())
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True
