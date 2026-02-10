#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#Example 1: Input: s = "racecar", t = "carrace"
#Output: true
#Example 2: Input: s = "jar", t = "jam"
#Output: false

#Method 1: Sort strings and compare:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            s=sorted(s)
            t=sorted(t)
            return s==t

#Method 2: HashMap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        else:
            countS, countT={},{}
            for i in range(len(s)):
                countS[s[i]]=countS.get(s[i], 0) + 1
                countT[t[i]]=countT.get(t[i], 0) + 1
            return countS==countT

#A hash map (also called a dictionary in Python) is a data structure that stores key-value pairs 
#and allows for fast access, insertion, and updates.
#It counts character frequencies for both strings into two separate hash maps.
#If these two frequency maps are identical, the strings are anagrams.
#Time C: O(m+n) & Space C: O(1)
