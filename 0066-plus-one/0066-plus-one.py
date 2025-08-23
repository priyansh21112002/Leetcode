class Solution:
    def plusOne(self, digit: List[int]) -> List[int]:
        n = len(digit)

        digit[-1] = digit[-1] + 1

        for i in range(n - 1, 0, -1):
            if digit[i] == 10:
                digit[i] = 0
                digit[i - 1] = digit[i - 1] + 1

        
        if digit[0] == 10:
            digit[0] = 0
            return [1] + digit
        
        return digit

        