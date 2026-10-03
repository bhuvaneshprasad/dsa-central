class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        mvp = 0

        for i, l in enumerate(s):
            if not stack and l == "(":
                stack.append(i)
            elif not stack and l == ")":
                stack.append(i)
                continue
            elif l == "(":
                stack.append(i)
            elif l == ")" and s[stack[-1]] == "(":
                stack.pop()
            elif l == ")":
                stack.append(i)

        if not stack:
            return len(s)

        mvp = stack[0]

        for i in range(1, len(stack)):
            distance = stack[i] - stack[i - 1] - 1
            mvp = max(mvp, distance)

        distance = len(s) - stack[-1] - 1
        mvp = max(mvp, distance)

        return mvp
