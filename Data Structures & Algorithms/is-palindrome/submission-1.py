class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for c in s:
            if c.isalnum():
                x += c
        x = x.lower().strip()
        i = 0
        j = len(x) - 1
        while i < j:
            start = x[i]
            end = x[j]
            if start == end:
                i += 1
                j -= 1
            else:
                return False
        return True
        