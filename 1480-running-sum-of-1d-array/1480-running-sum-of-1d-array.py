class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x1=0
        for i in range(len(nums)):
            x1+=nums[i]
            nums[i]=x1
        return nums