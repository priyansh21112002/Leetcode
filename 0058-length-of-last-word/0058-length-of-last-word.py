class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       i = len(s) - 1
       k = 0

       while i >= 0 and s[i] == " " :
            i = i - 1
        
       while s[i] != " " and i >= 0 :
            i = i - 1
            k = k + 1
       
       return k