#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#Example 1: Input: strs = ["act","pots","tops","cat","stop","hat"]
#Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

#Solution:
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))    # Sort the word to get the key
            anagram_map[sorted_word].append(word)  # Append the original word to the list for this key

        return list(anagram_map.values())          # Return all grouped anagram lists
