class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # nums1 = [4,1,2]
        # nums2 = [1,3,4,2]
        
        stack = []
        maps = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                maps[stack.pop()] = num
            stack.append(num)
        
        gt_nums = []
        for num in nums1:
            gt_nums.append(maps.get(num, -1))
        
        return gt_nums
