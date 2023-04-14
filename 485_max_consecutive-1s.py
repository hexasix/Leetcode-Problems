
# def findMaxConsecutiveOnes(nums: list[int]) -> int:
#     max = 0
#     count = 0
#     window = False
#     length = len(nums)
#     for i in range(len(nums)):
#         if i == 0 and nums[i] == 1:
#             window = True

#         if nums[i] == 1 and i != 0 and nums[i-1] != 1:
#             window = True

#         if window:
#             count = count+1

#         if (i+1) < length:
#             if nums[i+1] != 1 and window:
#                 window = False
#                 if count > max:
#                     max = count
#                 count = 0
#                 continue
#         elif i==length-1 and window:
#             if count>max:
#                 max=count

#     return max


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_consecutive = 0
    current_consecutive = 0
    for num in nums:
        if num == 1:
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 0
    return max_consecutive


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
