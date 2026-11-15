class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def findStuff(cur_val, path):
            temp=[]
            if cur_val == target:
                # zach = 0
                # for lst in temp:
                #     print(lst)
                #     print(path)
                #     if sorted(lst) != sorted(path):
                #         zach += 1
                # if zach == len(temp):
                return [path]
            for i in nums:
                if cur_val + i <= target:
                    temp += findStuff(cur_val + i, path + [i])
            return temp
        def pleaseSort(puta):
            newlst = []
            for i in puta:
                i.sort()
                z = 0
                for j in newlst:
                    if i != j:
                        z += 1
                if z == len(newlst):
                    newlst.append(i)
            return newlst


        return pleaseSort(findStuff(0,[]))
        # fionnita.append(findStuff(0,[]))
        # return fionnita

        