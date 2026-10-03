class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = None
        
        s = 0
        
        for l in range(0, k):
            s += nums[l]
        
        max_avg = s / k
        
        i, j = 1, k
        
        while j < len(nums):
            s = s - nums[i-1] + nums[j]
            
            avg = s / k
            if max_avg is None or avg > max_avg:
                max_avg = avg
            i += 1
            j += 1
        
        return max_avg
