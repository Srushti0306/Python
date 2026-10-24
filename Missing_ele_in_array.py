# OPTIMAL 
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n*(n + 1) // 2 - sum(nums)

# BETTER
# n=len(nums)
# for i in range(0, n+1):
#     freq[i]=0
# for num in nums:
#     freq[nums]=1
# for k,v in freq.items():
#     if v==0:
#         return k
