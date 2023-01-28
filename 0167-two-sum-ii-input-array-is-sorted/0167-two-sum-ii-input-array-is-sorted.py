class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            r=len(nums)-1
            while(i<r):
                sum=nums[i]+nums[r]

                if sum==target:
                    return [i+1,r+1]
                elif sum<target:
                    i+=1
                else:
                    r-=1