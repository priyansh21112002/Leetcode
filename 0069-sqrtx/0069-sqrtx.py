class Solution:
    def mySqrt(self, x: int) -> int:
        root = 1

        if x == 0:
            return 0
        
        if x <= 2:
            return 1


        for i in range(1, x + 1):
            if root > x:
                return i - 2
            root = i * i