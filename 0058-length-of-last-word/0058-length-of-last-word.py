class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       k = 0
       found = False

       for c in reversed(s):
        if c != " " :
            found = True
            k = k + 1
        
        elif found:
            break
        
       return k
