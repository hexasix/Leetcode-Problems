# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# class Solution:
#     def moveZeroes(nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         length = len(nums)
#         p_last = length - 1
#         wp=0
#         # p_last points to the last element that is not 0
#         for i in range(length-1, -1, -1):
#             if nums[i] != 0:
#                 p_last = i
#                 break
#         print("p_last=",p_last)
#         while wp<length:
#             if wp < p_last and nums[wp] == 0:
#                 for i in range(wp+1,p_last):
#                     print("line 30 nums=",nums)
#                     nums[i-1]=nums[i]

#                 temp=nums[p_last]
#                 nums[p_last]=0
#                 p_last-=1
#                 nums[p_last]=temp
#                 print("line 32 nums=",nums)
#                 continue
#             wp+=1


# two pointers
class Solution:
    def moveZeroes(nums: list[int]) -> None:
        length = len(nums)
        # two pointers
        readPointer = 0
        writePointer = 0
        while readPointer < length:
            if nums[readPointer] != 0:
                nums[readPointer], nums[writePointer] = nums[writePointer], nums[readPointer]
                writePointer += 1
            readPointer += 1
        return


nums = [0, 1, 0, 3, 12]# [1,3,12,0,0]
# nums=[0]
Solution.moveZeroes(nums)
print("nums=", nums)
