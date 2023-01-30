class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        x=str(x)
        if x[::-1]==y:
            return True
        return False