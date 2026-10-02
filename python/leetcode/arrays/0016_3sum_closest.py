# LeetCode 16 - 3Sum Closest
#
# Pattern: Sort + Two Pointers / Opposite Ends
# Sort the array, fix one value, and move the two pointers based on whether
# the current triplet sum is below or above the target.


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        close_match, close_match_diff = None, None
        for idx, num in enumerate(nums):
            left = idx + 1
            right = len(nums) - 1

            # [-1, 2, 1, -4] 1

            while left < right:
                num_sum = num + nums[left] + nums[right] # -3
                diff = target - num_sum # 4
                diff = diff if diff >= 0 else -diff

                if close_match is None and close_match_diff is None:
                    close_match = num_sum
                    close_match_diff = diff
                
                if diff < close_match_diff:
                    close_match = num_sum
                    close_match_diff = diff
                
                if diff == 0:
                    return target
                elif num_sum < target:
                    left += 1
                elif num_sum > target:
                    right -= 1
                    continue
                
        return close_match
