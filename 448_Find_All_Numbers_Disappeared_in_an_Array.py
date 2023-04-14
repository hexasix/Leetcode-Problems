# Given an array nums of n integers where nums[i]
# is in the range [1, n], return an array of all
#  the integers
# in the range [1, n]
# that do not appear in nums.

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Input: nums = [1,1]
# Output: [2]

# Too Slow
# class Solution:
#     def findDisappearedNumbers( nums: list[int]) -> list[int]:
#         length = len(nums)
#         arr = [i for i in range(1,length+1)]
#         result=[]
#         print("arr=",arr)
#         for i in arr:
#             if  i not in nums and i not in result:
#                 result.append(i)
#         return result

class Solution:
    def findDisappearedNumbers(nums: list[int]) -> list[int]:
        length = len(nums)
        ret=[]
        for index in range(length) :
            # x is the index of which the current iterated number represents
            x = (nums[index] % length)-1
            nums[x] += length
        for index,num in enumerate(nums):
            if num<=length:
                ret.append(index+1)
        return ret
nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
print(Solution.findDisappearedNumbers(nums))
