class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            temp1 = -1 * heapq.heappop(heap)
            temp2 = -1 * heapq.heappop(heap)
            if temp1 != temp2:
                temp = abs(temp1 - temp2)
                heapq.heappush(heap, -1 * temp)
        if heap:
            return -1 * heap[0]
        return 0