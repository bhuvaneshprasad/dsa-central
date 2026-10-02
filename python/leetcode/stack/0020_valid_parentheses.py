class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for i in s:
            if i not in map:
                stack.append(i)
            elif len(stack)>0 and stack[-1] == map[i]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False
