class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        alternate_total = 1
        zero_counter = 0
        for i in nums:
            if i == 0 and zero_counter == 0:
                total = total * i
                zero_counter += 1
            else:
                total = total * i
                alternate_total = alternate_total * i
            
        return_list = []
        for i in nums:
            if i == 0:
                return_list.append(alternate_total)
            else:
                return_list.append(total // i)
        return return_list