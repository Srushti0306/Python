# With Slicing
# def rightRotate(nums):
#     n=len(nums)
#     nums[:]=[nums[-1]]+nums[0:n-1]
#     return nums

# nums=[3,4,5,55,6,2,9]
# right_rotate=rightRotate(nums)
# print(right_rotate)

# Without Slicing
def rightRotate(nums):
    n=len(nums)
    temp=nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1]=nums[i]
    nums[0]=temp
    return nums

nums=[3,4,5,55,6,2,9]
right_rotate=rightRotate(nums)
print(right_rotate)

    