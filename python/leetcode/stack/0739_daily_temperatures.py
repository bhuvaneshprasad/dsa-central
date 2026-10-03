class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        better_tmp = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                better_tmp[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temp))
                        
        return better_tmp
