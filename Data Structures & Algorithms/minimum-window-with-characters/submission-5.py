class Solution:
    def minWindow(self, s: str, t: str) -> str:
        first = 0
        second = 0
        lookup = {}
        m = {}
        o = [0, len(s) - 1, float('inf')]

        for x in t:
            if x not in lookup:
                lookup[x] = 0
                m[x] = 0
            lookup[x] += 1

        while second != len(s):
            if s[second] in lookup:
                m[s[second]] += 1
                if m[s[second]] == lookup[s[second]]:
                    b = True
                    for k, v in m.items():
                        if v < lookup[k]:
                            b = False
                            break
                    while b is True:
                        if second - first < o[2]:
                            o = [first, second, second - first]
                        first += 1
                        if first > len(s) - 1:
                            b = False
                            break
                        if s[first-1] in lookup:
                            m[s[first-1]] -= 1
                            if m[s[first-1]] < lookup[s[first-1]]:
                                b = False
            second += 1
        return s[o[0]:o[1]+1] if o[2] != float('inf') else ""
        