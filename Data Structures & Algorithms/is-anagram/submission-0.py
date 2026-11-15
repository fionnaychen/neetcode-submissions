class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = sorted(s)
        tlist = sorted(t)
        print(slist)
        print(tlist)
        return slist == tlist