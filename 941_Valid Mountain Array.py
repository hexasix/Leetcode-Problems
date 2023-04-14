# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]




# Bookmark：Fix the following issue
# --------------------
#  !ATTENTION!
#  The Array needs to contain both increasing and decreasing.
#  If only one of em exits, it should return False
# 
# -------------------- 
def validMountainArray(arr: list[int]) -> bool:
    increasing_flag = True
    decreasing_flag = False
    is_valid_mountain =False 
    change_count=0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1] and increasing_flag:
            is_valid_mountain = True
            change_count=1
        elif arr[i] < arr[i-1] and increasing_flag:
            increasing_flag = False
            decreasing_flag = True
            change_count+=1
        elif arr[i] < arr[i-1] and decreasing_flag:
            is_valid_mountain=True
        elif arr[i] > arr[i-1] and decreasing_flag:
            is_valid_mountain = False
            break
        elif arr[i] == arr[i-1]:
            is_valid_mountain=False
            break

    if(increasing_flag==False and decreasing_flag==True and is_valid_mountain and change_count>=2):
        is_valid_mountain=True
    else:
        is_valid_mountain=False

    return is_valid_mountain

arr = [i for i in range(9,-1,-1)]
print("arr=",arr)
print(validMountainArray(arr))