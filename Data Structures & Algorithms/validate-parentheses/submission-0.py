class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        last_ind = -1
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                opens.append(s[i])
                last_ind += 1
            elif last_ind == -1:
                return False
            elif s[i] == '}':
                if opens[last_ind] != '{':
                    return False
                else:
                    opens = opens[:-1]
                    last_ind -= 1
            elif s[i] == ']':
                if opens[last_ind] != '[':
                    return False
                else:
                    opens = opens[:-1]
                    last_ind -= 1
            elif s[i] == ')':
                if opens[last_ind] != '(':
                    return False
                else:
                    opens = opens[:-1]
                    last_ind -= 1
        if len(opens) > 0:
            return False
        return True
        