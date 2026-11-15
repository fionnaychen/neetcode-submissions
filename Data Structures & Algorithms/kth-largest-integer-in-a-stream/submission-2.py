class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.my_heap = nums
        self.k = k
        if nums:
            heapq.heapify(self.my_heap)
            while self.my_heap and len(self.my_heap) > k:
                heapq.heappop(self.my_heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.my_heap, val)
        if len(self.my_heap) > self.k:
            heapq.heappop(self.my_heap)
        return self.my_heap[0]