# LeetCode 35 - Search Insert Position
#
# Pattern: Binary Search
# Search the sorted array by repeatedly checking the middle value.
# If the target is absent, left ends at the first valid insertion position.


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # [1,3,5,6] 2

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return left
