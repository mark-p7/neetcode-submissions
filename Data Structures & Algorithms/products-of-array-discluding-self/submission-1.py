class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 0
        hasZero = [False, False]
        for n in nums:
            if n != 0:
                p = n if p == 0 else p * n
            else:
                if hasZero[0] == True:
                    hasZero[1] = True
                else:
                    hasZero[0] = True
        
        o = []
        for n in nums:
            if hasZero[0]:
                o.append(0 if n != 0 or hasZero[1] else p)
            else:
                o.append(int(p / n))

        return o
        
            