class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycleLen = 2 * numRows - 2
        res = []

        for i in range(numRows):
            for j in range(i, len(s), cycleLen):
                res.append(s[j])
                # For middle rows, take the diagonal element
                if i != 0 and i != numRows - 1 and j + cycleLen - 2 * i < len(s):
                    res.append(s[j + cycleLen - 2 * i])

        return "".join(res)


