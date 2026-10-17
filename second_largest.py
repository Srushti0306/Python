# Brute Force Approach
# sort and then return arr[-2]

# Better Approach
# def second_largest(nums):
#     largest_num=float('-inf')
#     second_largest=float('-inf')
#     for i in range(0, len(nums)):
#         largest_num=max(largest_num, nums[i])
#     for i in range(0, len(nums)):
#         if nums[i]>second_largest and nums[i]!=largest_num:
#             second_largest=nums[i]
#     return second_largest

# nums=[23,44,32,34,-98]
# s_large=second_largest(nums)
# print(s_large)

# Optimal Approach 
nums=[33,45,67,345,223]
def second_largest(nums):
    largest=float('-inf')
    s_largest=float('-inf')
    for i in range(0, len(nums)):
        if nums[i]>largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest=nums[i]
    return s_largest
second_largest_ele=second_largest(nums)
print(second_largest_ele)