class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        f = s1.split(" ")
        s = s2.split(" ")
        first = {}
        second = {}

        for word in f:
            if word not in first:
                first[word] = 0
            first[word] += 1

        for word in s:
            if word not in second:
                second[word] = 0
            second[word] += 1

        o = []

        for word in first:
            if first[word] < 2 and word not in second:
                o.append(word)
        
        for word in second:
            if second[word] < 2 and word not in first:
                o.append(word)
        
        return o