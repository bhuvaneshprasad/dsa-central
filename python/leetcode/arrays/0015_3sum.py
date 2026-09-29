class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []

        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == -num:
                    triplets.append([num, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum < -num:
                    left += 1
                else:
                    right -= 1

        return triplets
