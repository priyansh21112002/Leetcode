class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax=1
        curMin=1
        res=max(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                curMax,curMin=1,1
                continue
            tmp=curMax*nums[i]
            curMax=max(nums[i]*curMax,nums[i]*curMin,nums[i])
            curMin=min(tmp,nums[i]*curMin,nums[i])
            res=max(res,curMax)
        return res       