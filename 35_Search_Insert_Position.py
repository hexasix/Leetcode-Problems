# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution:
    def searchInsert(nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = (low+high)//2
        while low <= high:
            if (nums[mid] == target):
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            mid = (low+high)//2
        print("mid=", mid+1)
        return mid+1


nums = [1, 3, 5, 6]
print(Solution.searchInsert(nums, 7))

