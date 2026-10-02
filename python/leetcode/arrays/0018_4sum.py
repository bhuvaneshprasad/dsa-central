class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums = sorted(nums)
        four_sums = []
        #  [1,0,-1,0,-2,2] 0
        for i, num1 in enumerate(nums):
            if i> 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, len(nums)):
                if j>i+1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    four_sum = num1 + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        four_sums.append([num1, nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif four_sum > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return four_sums
