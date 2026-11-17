import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] = map[num] + 1
            
        min_heap = [(freq, num) for num, freq in map.items()]

        heapq.heapify_max(min_heap)

        output = []
        for i in range(0, k):
            popped = heapq.heappop_max(min_heap)
            output.append(popped[1])
        
        return output
