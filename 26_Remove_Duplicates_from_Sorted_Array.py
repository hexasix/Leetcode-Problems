def removeDuplicates(nums: list[int]) -> int:
    # wrong answer
    # length = len(nums)
    # k = length
    # pointer_end = length-1
    # for index, num in enumerate(nums, 1):
    #     if index>pointer_end:
    #         break

    #     while nums[index] == nums[index-1]:
    #         for i in range(index,pointer_end+1):
    #             nums[i-1] = nums[i]
    #         pointer_end-=1
    #         k-=1
    # return pointer_end+1

    if not nums:
        return 0

    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
            
    return j + 1



#k=2 nums=[1,2,_]
# nums = [1,1,2]   
# print("k=",removeDuplicates(nums),"nums=",nums)
# 5, nums = [0,1,2,3,4,_,_,_,_,_]
# nums = [0,0,1,1,1,2,2,3,3,4]


nums=[1,1]
print("k=",removeDuplicates(nums),"nums=",nums)