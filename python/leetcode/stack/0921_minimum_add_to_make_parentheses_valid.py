class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        unmatched_open = 0
        unmatched_close = 0

        for p in s:
            if p == "(":
                unmatched_open += 1
            elif p == ")" and unmatched_open > 0:
                unmatched_open -= 1
            elif p == ")" and unmatched_open == 0:
                unmatched_close += 1

        return unmatched_open + unmatched_close
