class Solution:
    def removeElement(nums: list[int], val: int) -> int:
        writePointer = 0 
        for i in range( len(nums) ):
            if nums[i]!= val :
                nums[writePointer] = nums[i]
                writePointer+=1
        return writePointer
