# Given an array of integers nums and
# an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

# class Solution:
#     def twoSum( nums: list[int], target: int) -> list[int]:#This is OK but too slow
#         length = len(nums)
#         for i in range(length):
#             for j in range(length):
#                 if(i==j): continue
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]
# return 1
# The correct solution of this is to use a hashmap.

class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:  # This is OK but too slow
        length = len(nums)
        hashMap = {}
        for i in range(length):
            hashMap[nums[i]] = i
        print(hashMap)
        for i in range(length):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]]


# nums = [2,7,11,15]
# target = 9
# Output: [1,2]
# nums = [0, 4, 3, 0]
# target = 0
nums=[2,7,11,15]
target=9
print(Solution.twoSum(nums, target))
