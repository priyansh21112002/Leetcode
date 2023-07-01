class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        below=[1]*n

        for i in range(m-1):
            above=[1]*n

            for j in range(n-2,-1,-1):
                above[j]=below[j]+above[j+1]
            below=above

        return below[0]

