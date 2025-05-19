#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#Please implement encode and decode functions.

#Example 1: Input: ["neet","code","love","you"]
#Output:["neet","code","love","you"]

#Solution:
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            for letter in word:
                res.append(str(ord(letter)))  # convert to ASCII and then to string
                res.append(",")               # use comma to separate ASCII codes
            res.append("@")                   # use '@' to mark end of word
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        final = []
        current_word = []
        num = ""
        for char in s:
            if char.isdigit():
                num += char
            elif char == ",":
                if num:
                    current_word.append(chr(int(num)))
                    num = ""
            elif char == "@":
                final.append("".join(current_word))
                current_word = []
        return final

# Example usage:
sol = Solution()
encoded = sol.encode(["hello", "world"])
print("Encoded:", encoded)

decoded = sol.decode(encoded)
print("Decoded:", decoded)

