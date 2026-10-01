# LeetCode 27 - Remove Element
#
# Pattern: Two Pointers (shrink from end)
# Keep valid elements in the front portion of the array. When the left value
# matches the target, discard from the right side or swap in an unchecked value.


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        # [3,2,2,3] 3
        while left <= right:
            temp = None
            if nums[left] == val:
                if nums[right] == val:
                    right -= 1
                else:
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                    right -= 1
            else:
                left += 1
                count += 1
        
        return count
