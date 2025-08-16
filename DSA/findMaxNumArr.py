def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num        
numbers= [11,22,44,77,33]    
print("biggest number is:", find_max(numbers))      