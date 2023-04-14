# Given an array arr, replace every element in that array with
# the greatest element among the elements to its right,
# and replace the last element with -1.
# After doing so, return the array.

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Brute-force Solution (Time-Limit Exceeded)
# class Solution:
#     def replaceElements(arr: list[int]) -> list[int]:
#         max = None
#         for index, item in enumerate(arr):
#             if (index < (len(arr)-1)):
#                 max = arr[index+1]
#                 for i in range(index+1, len(arr)):
#                     if arr[i]>max:
#                         max=arr[i]
#                 arr[index] = max;
#             elif index==len(arr)-1:
#                 arr[index]=-1


class Solution:
    def replaceElements(arr: list[int]) -> list[int]:
        max = -1
        temp = 0
        length = len(arr)
        for i in range(length-1, -1, -1):
            temp = arr[i]
            arr[i] = max
            if temp>max:
                max=temp
        return arr


arr = [17,18,5,4,6,1]
Solution.replaceElements(arr)
print(arr)
