class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            k = str(sorted(s))
            if k not in m:
                m[k] = []
            m[k].append(s)
        
        return [v for x, v in m.items()]