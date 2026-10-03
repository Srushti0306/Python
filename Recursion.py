# Recursion Theory
# 2 types head and tail recursion

# Head Recursion - Do work first and then call fun
# def greet():
#     if count==4:
#         return 
#     print("Srushti")
#     count+=1
#     greet()

# # Tail Recursion - Call fun and then call fun
# def greet():
#     if count==4:
#         return
#     count+=1
#     greet()
#     print("Srushti")

# #Parameterized recursion
# def fun(sum,i,N):
#     if i>N:
#         print(sum)
#         return 
#     fun(sum+i,i+1,N)

# Function recursion
def fun(N):
    if N==1:
        return 1
    return N + fun(N-1)
print(fun(4))