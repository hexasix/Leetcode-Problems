# Given an integer array nums,
# return the third distinct maximum number in this array.
# If the third maximum does not exist,
# return the maximum number.

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2
# (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.
class Solution:
    def thirdMax(nums: list[int]) -> int:
        max = 0
        reverseNums = sorted(nums, reverse=True)
        writePointer = 0
        readPointer = 1
        max = reverseNums[0]
        length= len(reverseNums)    
        setnums = set(nums)
        print(setnums)
        if(len(setnums)<3):
            return max
        print("reverseNUms=",reverseNums)
        while readPointer < length:
            if reverseNums[readPointer]!=reverseNums[writePointer]:
                writePointer+=1
                reverseNums[writePointer]= reverseNums[readPointer]
            readPointer+=1
        print(reverseNums)
        return reverseNums[2]
# 先倒排序
# 然后把所有独特的数字放到数组的最前面
# 变成一个单独的数组
# 长度小于3  直接返回最大值
# 如果长度长度大于等于三   返回第三位   也就是index==2的值
nums = [1,1,2]# 2
# print(Solution.thirdMax(nums))