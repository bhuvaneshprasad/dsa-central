# LeetCode 71: Simplify Path
# https://leetcode.com/problems/simplify-path/
#
# Pattern: Stack / LIFO - path processing
# Time: O(n)
# Space: O(n)


class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        stack = []
        for dir in dirs:
            if dir == "" or dir == "/" or dir == ".":
                continue
            elif dir == "..":
                if len(stack) > 0:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(dir)
        
        return "/" + "/".join(stack)
