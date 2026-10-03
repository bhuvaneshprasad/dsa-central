class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = "aeiou"
        maxc = 0
        mc = 0
        for i in s[:k]:
            if i in v:
                mc += 1

        maxc = mc

        i, j = 1, k

        while j < len(s):
            if s[i - 1] in v:
                mc -= 1

            if s[j] in v:
                mc += 1
                if mc > maxc:
                    maxc = mc
            i += 1
            j += 1

        return maxc
