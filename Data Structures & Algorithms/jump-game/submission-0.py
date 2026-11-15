class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        step = nums[0]
        if step == 0:
            return False
        counter = False
        for i in range(1,step+1):
            if i < len(nums):
                if self.canJump(nums[i:]):
                    counter = True
        return counter