from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if sorted(word1)==sorted(word2):
            return True
        
        else:
            c1=Counter(word1)
            c2=Counter(word2)
           # print(c1,c2)
            if c1.keys()!=c2.keys():
                return False
            else:
                if sorted(list(c1.values())) != sorted(list(c2.values())):
                    return False
        return True
        