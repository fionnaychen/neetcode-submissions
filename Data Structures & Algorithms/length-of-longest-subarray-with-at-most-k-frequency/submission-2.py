class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        counts = {}
        l, r = 0,0

        answer = 0

        for i, num in enumerate(nums):
            r = i

            counts[num] = counts.get(num,0)+1
            while counts[num] > k:
                counts[nums[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)
        
        return answer
            

            

            


