
class Solution:
    def moveZeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p_last = length - 1
        wp=0
        # p_last points to the last element that is not 0
        for i in range(length-1, -1, -1):
            if nums[i] != 0:
                p_last = i
                break
        print("p_last=",p_last)
        while wp<length:
            if wp < p_last and nums[wp] == 0:
                for i in range(wp+1,p_last):
                    print("line 30 nums=",nums)
                    nums[i-1]=nums[i]

                temp=nums[p_last]
                nums[p_last]=0
                p_last-=1
                nums[p_last]=temp
                print("line 32 nums=",nums)
                continue
            wp+=1