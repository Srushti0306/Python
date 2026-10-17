nums=[33,45,-89,2,1]

def large_Element(nums):
    largest_num=float('-inf')
    for i in range(0, len(nums)):
        largest_num=max(largest_num, nums[i])
    return largest_num
largest=large_Element(nums)
print(largest)