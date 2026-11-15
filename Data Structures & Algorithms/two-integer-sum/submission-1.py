class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}
        for i in range(len(nums)):
            if nums[i] in indMap:
                return [indMap[nums[i]],i]
            indMap[(target - nums[i])] = i
        return 'poop'
        