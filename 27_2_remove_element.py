# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k,
#  to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
#  The remaining elements of nums are not important as well as the size of nums.
# Return k.
class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        length = len(nums)
        readPointer = writePointer = 0
        while readPointer < length:
            if (nums[readPointer] != val):
                nums[readPointer], nums[writePointer] = nums[writePointer], nums[readPointer]
                writePointer+=1
            readPointer+=1
        return writePointer

nums = [3,2,2,3]
val = 3
result=Solution.removeElement(nums,val)
print("result=",result,"nums=",nums)
