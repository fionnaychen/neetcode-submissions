class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # setList = set()
        setDict = {}
        for s in strs:
            # st = set(s)
            sorted_s = ''.join(sorted(s))
            if sorted_s in setDict:
                setDict[sorted_s].append(s)
            else:
                setDict[sorted_s] = [s]   
                # setList.add(st) 
        return_list = []
        for key in setDict:
            return_list.append(setDict[key])
        return return_list