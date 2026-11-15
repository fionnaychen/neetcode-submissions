class Solution:
    def yuuk(self, list1):
        x = list1[0]
        y = list1[1]
        temp = math.sqrt(x**2 + y**2)
        return temp


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[-1 * self.yuuk(i), i[0], i[1]] for i in points]
        heapq.heapify(dists)
        while len(dists) > k:
            heapq.heappop(dists)
        return [[i[1], i[2]] for i in dists]
                    