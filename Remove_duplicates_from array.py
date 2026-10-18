# BRUTE FORCE
# def removeDuplicates(nums):
#     freq_map={}
#     for i in range(0, len(nums)):
#         freq_map[nums[i]]=0 #If not in dict, add in doct the key and value, key as num[i] and value as 0
#     j=0
#     for k in freq_map:
#         nums[j]=k
#         j+=1
#     return j

# nums=[1,1,2,2,2,3,3,3,4,4,4,4,5,5]
# duplicates=removeDuplicates(nums)
# print(duplicates)    

# OPTIMAL APPROACH - using 2 pointer approach
def removeDuplicates(nums):
    n=len(nums)
    if n==1:
        return 1
    i=0; j=i+1
    while j<n:
        if nums[i]!=nums[j]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1

nums=[1,1,2,2,2,3,3,3,4,4,4,4,5,5]
duplicates=removeDuplicates(nums)
print(duplicates) 

