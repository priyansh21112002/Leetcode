class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        # helper to reverse a section in place
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1

        # 1. reverse all
        reverse(0, n-1)
        # 2. reverse first k
        reverse(0, k-1)
        # 3. reverse n-k
        reverse(k, n-1)
