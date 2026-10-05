class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        current = 0

        for char in s:
            if char == "(":
                stack.append(current)
                current = 0
            elif char == ")":
                previous = stack.pop()
                if current == 0:
                    current = previous + 1
                else:
                    current = previous + 2 * current

        return current
