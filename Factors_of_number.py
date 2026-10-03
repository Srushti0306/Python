#brute force
# num=10
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)
# print(result)

# Better Approach- Go till half of num and then add num itself in list
# num=10
# result=[]
# for i in range(1,(num+//2) + 1):
#     if num%i==0:
#         result.append(i)
# result.append(num)--> to add num itself
# print(result)

# Optimized sol
from math import sqrt

num=10
result=[]

for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result.append(i)
        if num//i!=i:
            result.append(num//i)
result.sort()
print(result) 