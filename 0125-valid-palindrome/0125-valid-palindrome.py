class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=[]
        for i in range(len(s)):
            if s[i].isalpha()==True or s[i].isdigit()==True:
                x.append(s[i].lower())
        #print(x)
        return True if x[::-1]==x else False