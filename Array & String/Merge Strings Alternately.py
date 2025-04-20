""" You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c d"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1)>len(word2):  #Word1 > Word2
            maxlen=len(word2)
            arr=""
            for i in range(0,maxlen):
                arr+=word1[i]      #Append one letter of both words
                arr+=word2[i]
            
            for j in range(maxlen,len(word1)):
                arr+=word1[j]      #Append all letters of Word 1
            return arr
           
        
        elif len(word1)<len(word2):    #Word2 > Word1
            maxlen=len(word1)
            arr=""
            for i in range(0,maxlen):
                arr+=word1[i]          #Append one letter of both words
                arr+=word2[i]
            
            for j in range(maxlen,len(word2)):
                arr+=word2[j]          #Append all letters of Word 2
            return arr
        
        else:                          #Both words equal length
            arr=""
            for i in range(0,len(word1)):
                arr+=word1[i]          #Append one letter of both words
                arr+=word2[i]
            return arr
        
 """Improvements: Use a while statement to fit all 3 cases in same loop instead of solving each individually
