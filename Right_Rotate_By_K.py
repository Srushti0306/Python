class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverse(nums, n - k, n - 1)  # reverse k elements
        self.reverse(nums, 0, n - k - 1)  # reverse remaining elements
        self.reverse(nums, 0, n - 1)  # reverse whole array


# BRUTE FORCE
# rotations=k%n
# for _ in range(0, rotations):
#     e=nums.pop()
#     nums.insert(0,e)

# With Slicing
# nums[:]=nums[n-k:]+nums[:n-k]