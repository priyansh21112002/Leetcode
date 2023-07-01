class Solution:
    def jump(self, nums: List[int]) -> int:
        goal=len(nums)-1
        res=0
        l,r=0,0

        while r<goal:
            f=0

            for i in range(l,r+1):
                f=max(f,i+nums[i])

            l=r+1
            r=f
            res+=1

        return res
