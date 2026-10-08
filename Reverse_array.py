# Reverse Array using recursion

def reverse_array(arr,left,right):
    if left>=right:
        return
    arr[left],arr[right]=arr[right],arr[left]
    reverse_array(arr,left+1 ,right-1)  

arr=[1,2,3,4,5,6,7,8]
reverse_array(arr, 2,6)
print(arr)