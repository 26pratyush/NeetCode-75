#Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
#Please implement encode and decode functions.

#Example: Input: ["neet","code","love","you"] -> "neetcodeloveyou"
#Output:"neetcodeloveyou" -> ["neet","code","love","you"]

#Solution(Naive approach using a non-ascii character as a delimiter):
def encode(self, strs: List[str]) -> str:
    res=""
    for str in strs:
        res+=str
        res+="漢"
    return res

def decode(self, s: str) -> List[str]:
    res=[]
    string=""
    for char in s:
        if char=="漢":
            res.append(string)
            string=""

        else:
            string+=char            
    return res
