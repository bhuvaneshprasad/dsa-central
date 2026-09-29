# LeetCode 26 - Remove Duplicates from Sorted Array
#
# Pattern: Two Pointers (read/write)
# The array is sorted, so duplicates are adjacent. Scan each value and
# write only new unique values into the front of the same list.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_num = None
        current_idx = 0
        for num in nums:
            if current_num is None:
                current_num = num
                nums[current_idx] = num
                current_idx += 1
            if num == current_num:
                continue
            current_num = num
            nums[current_idx] = num
            current_idx += 1

        return current_idx
