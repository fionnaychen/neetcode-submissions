class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_ind_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in nums_ind_dict:
                return [nums_ind_dict[diff], i]
            nums_ind_dict[nums[i]] = i            