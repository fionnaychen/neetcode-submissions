class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = 0
        ri = len(s) - 1

        while li < ri:
            left = s[li]
            right = s[ri]
            if not left.isalnum():
                li += 1
                left = s[li]
                continue
            if not right.isalnum():
                ri -= 1
                right = s[ri]
                continue
            
            if left.lower() != right.lower() \
            and left.isalnum() and right.isalnum() \
            and li < ri:
                print(left, right)
                return False
            
            li += 1
            ri -= 1

        return True
            

        