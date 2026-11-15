class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap: key is num, value is index
        hashy = {}
        for i in range(len(nums)):
            if target - nums[i] in hashy:
                return [hashy[target - nums[i]], i]
            else:
                hashy[nums[i]] = i
        
        