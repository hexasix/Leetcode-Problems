def removeElement(nums: list[int],val:int) -> int:
    length_nums = len(nums)
    pointer_end = length_nums-1
    temp = None
    for index,item in enumerate(nums):

        while nums[pointer_end] == val and pointer_end>0:
            pointer_end-=1
        
        if nums[pointer_end] == val and pointer_end == 0:
            return 0
        
        if index>=pointer_end:
            break

        if item == val:
            temp = nums[index]
            nums[index] = nums[pointer_end]
            nums[pointer_end] = temp
    return pointer_end+1

nums = [0,1,2,2,3,0,4,2]
val=2
print("k=",removeElement(nums,val),"nums=",nums)
