# METHOD 1
# nums=[2,3,4,4,4,67,3,55,22,3,1,2]

# freq_map={}
# for i in range(0, len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]]+=1
#     else:
#         freq_map[nums[i]]=1

# print(freq_map[7])

# METHOD 2
# GET fun goes and checks in the dict if the key and its corresponding value exsits 
# and if yes it returns value or else return 0
nums=[2,3,4,4,4,67,3,55,22,3,1,2]

hash_map={}
for i in range(1, len(nums)):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1

print(hash_map[55])

