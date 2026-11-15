class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if target < nums[middle]:
                right = middle - 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_list, right_list = 0, len(matrix) - 1
        while left_list <= right_list:
            middle_list = (left_list + right_list) // 2
            if target < matrix[middle_list][0]:
                right_list = middle_list - 1
            elif target > matrix[middle_list][-1]:
                left_list = middle_list + 1
            else:
                return self.search(matrix[middle_list], target)
        return False


   
        