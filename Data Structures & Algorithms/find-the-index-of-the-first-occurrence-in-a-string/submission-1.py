class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0, len(haystack)):
            cur = 0
            while needle[cur] == haystack[i + cur]:
                cur += 1
                if cur == len(needle):
                    return i
                if i + cur >= len(haystack):
                    return -1

        return -1
