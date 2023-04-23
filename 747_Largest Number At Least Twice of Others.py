class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
    
        for i in range(len(nums)):
            if(nums[i]==maxNum):
                index = i
                continue
            if((nums[i]<<1) > maxNum):
                return -1
        return index