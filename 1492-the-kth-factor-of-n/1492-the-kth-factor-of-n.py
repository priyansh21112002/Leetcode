class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        x=[]
        for i in range(1,n+1):
            if (n%i==0):
                x.append(i)
        if len(x)<k:
            return -1
        return x[k-1]