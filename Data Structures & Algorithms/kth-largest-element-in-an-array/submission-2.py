class Solution:
    def quickSort(self, lst):
        if len(lst) > 1:
            pointer = 0
            pivot = lst[-1]
            for i in range(len(lst) - 1):
                if lst[i] <= pivot:
                    tmp = lst[i]
                    lst[i] = lst[pointer]
                    lst[pointer] = tmp
                    pointer += 1
            lst[-1] = lst[pointer]
            lst[pointer] = pivot
            return self.quickSort(lst[:pointer]) + [lst[pointer]] + self.quickSort(lst[pointer+1:])
        else:
            return lst

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick sort
        nums = self.quickSort(nums)
        print(nums)
        return nums[-k]

        