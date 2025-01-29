class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        k = 0
        while k < len(t) and i < len(s):
            if t[k] == s[i]:
                i += 1
            k += 1
        if i == len(s):
            return True
        else:
            return False

