class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        s = set()
        last = 0
        missing = -1
        duplicate = 0
        for num in nums:
            if num in s:
                duplicate = num
            else:
                s.add(num)
                if last + 1 != num:
                    missing = last + 1
            last = num
        return [duplicate, missing if missing > 0 else nums[len(nums) - 1] + 1]