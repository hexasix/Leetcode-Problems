class Solution:
    def thirdMax(self,nums: list[int]) -> int:
        nums.sort(reverse=True)
        count=1
        previousUniqueElement =nums[0]
        for i in range(len(nums)):
            if(nums[i]!=previousUniqueElement):
                count+=1
                previousUniqueElement=nums[i]
            if(count==3):
                return nums[i]
        if(count<3):
            return nums[0]