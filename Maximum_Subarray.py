class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total=0; maxi=float("-inf")
        n=len(nums)
        for i in range(0,n):
            total=total+nums[i]
            maxi=max(total,maxi)
            if total<0:
                total=0
        return maxi
        