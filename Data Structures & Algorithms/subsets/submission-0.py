class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        big_daddy_list = [[]]
        for i in nums:   
            temp = []
            for j in big_daddy_list:
                temp.append(j + [i])
            big_daddy_list = big_daddy_list + temp
        return big_daddy_list
        