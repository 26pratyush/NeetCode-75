#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

#Example 1: Input: strs = ["act","pots","tops","cat","stop","hat"]
#Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

#Solution:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict, Counter

        anagram_map = defaultdict(list)
        for word in strs:
            count = Counter(word)                    # Count character frequencies
            key = tuple(sorted(count.items()))       # Convert to a hashable key
            anagram_map[key].append(word)
        return list(anagram_map.values())

# This solution groups anagrams by counting each word’s character frequencies using Counter.
# It converts the frequency dictionary into a sorted tuple (key) so it can be used as a dictionary key (as tuple is immutable).
# Words with the same character counts share the same key and are grouped together in anagram_map.
