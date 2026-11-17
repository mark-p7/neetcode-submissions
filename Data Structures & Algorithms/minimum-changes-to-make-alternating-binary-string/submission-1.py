class Solution:
    def minOperations(self, s: str) -> int:
        r = "1"
        c = "0"
        count = 0
        for i in range(0, len(s)):
            if s[i] != c:
                count = count + 1
            c, r = r, c
        return count if count < (len(s) - count) else len(s) - count
