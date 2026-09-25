# def is_armstrong_number(n):
#     nums=n
#     count=0
#     result=0
#     while nums>0:
#         count+=1
#         nums//=10 #divides the number by 10

#     nums =n 
#     while nums>0:
#         last_digit = nums % 10
#         result += last_digit ** count
#         nums //= 10

#     if result == n:
#         return True
#     else:
#         return False

# print(is_armstrong_number(13))

# Alternate way

def is_armstrong_number(n):
    num=n
    count=len(str(n))
    result=0
    while num>0:
        last_digit=num%10
        result=last_digit**count+result
        num//=10
    if result==n:
        return True
    else:
        return False
print(is_armstrong_number(53))
