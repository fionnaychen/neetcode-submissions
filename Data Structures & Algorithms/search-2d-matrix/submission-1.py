import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = np.ravel(matrix)
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                return True
        return False