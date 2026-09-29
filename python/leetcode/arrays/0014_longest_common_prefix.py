# LeetCode 14 - Longest Common Prefix
#
# Approach: Vertical scanning
# The common prefix cannot be longer than the shortest string.


# Solution 1 - My solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_str = None
        for s in strs:
            if not shortest_str:
                shortest_str = s
            if len(shortest_str) > len(s):
                shortest_str = s

        longest_common_prefix = ""
        for i in range(len(shortest_str)):
            current_letter = shortest_str[i]
            for s in strs:
                if not s:
                    return ""
                if s[i] != current_letter:
                    return longest_common_prefix
            longest_common_prefix += current_letter

        return longest_common_prefix


# Solution 2 - Same approach with Python's min() to select the shortest string.
class SolutionUsingMin:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest_str = min(strs, key=len)

        longest_common_prefix = ""

        for i in range(len(shortest_str)):
            current_letter = shortest_str[i]

            for s in strs:
                if s[i] != current_letter:
                    return longest_common_prefix

            longest_common_prefix += current_letter

        return longest_common_prefix
